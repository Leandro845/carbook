from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from cars.models import Car, CarComment
from .tasks import make_a_trip_task
from django.contrib import messages
from django.core.serializers import deserialize
from datetime import datetime
from django.db.models import Count


def pricing(request):
    # Retrieve all cars and order them by ID in descending order.
    cars = Car.objects.all().order_by('-id')

    # Paginate the cars, showing 6 per page.
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    obj_list = paginator.get_page(page)

    return render(request, 'pricing.html', {'obj_list': obj_list})


def car_list(request):
    # Retrieve all cars and order them by ID in descending order.
    cars_ = Car.objects.all().order_by('-id')

    # Paginate the cars, showing 12 per page.
    paginator = Paginator(cars_, 12)
    page = request.GET.get('page')
    obj_list = paginator.get_page(page)

    return render(request, 'cars.html', {'obj_list': obj_list})


def car_detail(request, pk):
    # Retrieve a single car based on its primary key.
    car = get_object_or_404(Car, pk=pk)
    # Retrieve related cars, excluding the current one.
    related_cars = Car.objects.exclude(id=car.id)[:3]

    # Get the total number of reviews.
    total_reviews = CarComment.objects.count()

    # Aggregate and count reviews by star rating.
    stars_list = CarComment.objects.values('starts_comment__stars').annotate(count=Count('id')).order_by('-starts_comment__stars')

    return render(request, 'car-single.html', {'car': car, 'related_cars': related_cars, 'total_reviews': total_reviews, 'stars_list': stars_list})


def book_car(request, pk):
    # Retrieve a single car based on its primary key.
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'book_car.html', {'car': car})


def available_cars(request):
    # Retrieve all cars and order them by ID in descending order.
    cars = Car.objects.all().order_by('-id')
    return render(request, 'available_cars.html', {'cars': cars})


def make_a_trip(request):
    if request.method == 'GET':
        # Display the home page if the request is a GET request.
        return render(request, 'home.html')
    
    elif request.method == 'POST':
        # Retrieve and format the trip details from the POST request.
        pick_up_location = request.POST.get('pick-up-location')
        drop_off_location = request.POST.get('drop-off-location')
        pick_up_date = request.POST.get('pick-up-date')
        drop_off_date = request.POST.get('drop-off-date')

        # Convert date formats from MM/DD/YYYY to YYYY-MM-DD.
        pick_up_date = datetime.strptime(pick_up_date, '%m/%d/%Y').strftime('%Y-%m-%d')
        drop_off_date = datetime.strptime(drop_off_date, '%m/%d/%Y').strftime('%Y-%m-%d')

        # Call the Celery task to find available cars.
        available_cars_task = make_a_trip_task.delay(
            pick_up_location,
            pick_up_date,
            drop_off_date
        )

        # Wait for the task to complete and get the result.
        available_cars_serialized = available_cars_task.get()

        if available_cars_serialized:
            # Deserialize the result into car objects.
            available_cars = [obj.object for obj in deserialize('json', available_cars_serialized)]

            if available_cars:
                # Paginate the available cars, showing 12 per page.
                paginator = Paginator(available_cars, 12)
                page = request.GET.get('page')
                obj_list = paginator.get_page(page)

                return render(request, 'available_cars.html', {'obj_list': obj_list})
            else:
                messages.error(request, 'We do not have any vehicles available that fit your search parameters.')
                return redirect('make_a_trip')
        
        else:
            messages.error(request, 'We do not have any vehicles available that fit your search parameters.')
            return redirect('make_a_trip')

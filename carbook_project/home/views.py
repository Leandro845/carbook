from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car
from branch_cities.models import BranchCities
from branch_cities.models import BranchCities


def home(request):
    cars = Car.objects.all()
    carroser_part = cars.order_by('-id')[:3]
    qnt_cars = len(cars)

    branchs = BranchCities.objects.all()
    qnt_branchs = len(branchs)

    locations = BranchCities.objects.values_list('name_city', flat=True)

    vars_ = {
        'carroser_part': carroser_part,
        'qnt_cars': qnt_cars,
        'qnt_branchs': qnt_branchs,
        'locations': locations
    }

    return render(request, 'index.html', vars_)

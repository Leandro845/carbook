from django.shortcuts import render
from cars.models import Car

def about(request):
    # Fetch all cars from the database.
    cars = Car.objects.all()
    
    # Calculate the total number of cars.
    qnt_cars = len(cars)
    
    # Render the 'about.html' template with the total number of cars.
    return render(request, 'about.html', {'qnt_cars': qnt_cars})

def services(request):
    # Render the 'services.html' template.
    return render(request, 'services.html')

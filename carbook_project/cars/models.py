from django.db import models
from car_category.models import Brand, TransmissionType, Fuel
from branch_cities.models import BranchCities


class Car(models.Model):
    category = models.ForeignKey(Brand, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=20)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    transmission = models.ForeignKey(TransmissionType, on_delete=models.CASCADE) 
    seats = models.IntegerField()
    luggage = models.IntegerField()
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    pricing_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    pricing_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    pricing_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars', blank=True, null=True)
    description = models.TextField(max_length=1200)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    pick_up_date = models.DateTimeField(blank=True, null=True)
    drop_off_date = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(BranchCities, on_delete=models.DO_NOTHING)

    airconditions = models.BooleanField(default=False)
    child_seat = models.BooleanField(default=False)
    luggage = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    seat_beat = models.BooleanField(default=False)
    sleeping_bed = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    onboard_computer = models.BooleanField(default=False)
    audio_input = models.BooleanField(default=False)
    long_term_trips = models.BooleanField(default=False)
    car_kit = models.BooleanField(default=False)
    remote_central_locking = models.BooleanField(default=False)
    climate_control = models.BooleanField(default=False)

    def __str__(self):
        return self.car_name
    


class Rating(models.Model):
    stars = models.IntegerField()



class CarComment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    comment = models.TextField(max_length=1200)
    created_at = models.DateTimeField(auto_now_add=True)

    starts_comment = models.ForeignKey(Rating, on_delete=models.DO_NOTHING) 

    
    def comment(self):
        return f'{self.car} - {self.user}'
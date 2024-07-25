from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TransmissionType(models.Model):
    name_transmission = models.CharField(max_length=15)

    def __str__(self):
        return self.name_transmission
    
class Fuel(models.Model):
    name_fuel = models.CharField(max_length=15)

    def __str__(self):
        return self.name_fuel
    

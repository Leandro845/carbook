from django.db import models


class BranchCities(models.Model):
    name_city = models.CharField(max_length=20)

    def __str__(self):
        return self.name_city

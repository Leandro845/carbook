from django.db import models
#from django.contrib.auth.models import User
from cars.models import Brand


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name_user = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


    def __str__(self):
        return self.name_user
    
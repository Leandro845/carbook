from django.contrib import admin
from .models import Car, CarComment, Rating


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'car_name')
    list_display_links = ('id', 'category', 'car_name')
    search_fields = ('category', 'car_name')
    list_filter = ('category', 'car_name')
    list_per_page = 10


class CarCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user', 'created_at')
    list_display_links = ('id', 'car', 'user', 'created_at')
    search_fields = ('car', 'user')
    list_filter = ('car', 'user')
    list_per_page = 10



admin.site.register(Car, CarAdmin)
admin.site.register(CarComment, CarCommentAdmin)
admin.site.register(Rating)

                          
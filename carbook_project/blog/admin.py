from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'car_brand')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'date', 'car_brand')
    list_filter = ('title', 'date', 'car_brand')
    list_per_page = 10


class ComentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_user', 'email', 'created')
    list_display_links = ('id', 'name_user')
    search_fields = ('name_user', 'email', 'created')
    list_filter = ('name_user', 'email', 'created')
    list_per_page = 10


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, ComentAdmin)
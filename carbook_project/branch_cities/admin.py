from django.contrib import admin
from .models import BranchCities


class AdminBranchCities(admin.ModelAdmin):
    list_display = ('id', 'name_city')
    list_display_links = ('id', 'name_city')
    search_fields = ('name_city',)
    list_per_page = 12


admin.site.register(BranchCities, AdminBranchCities)

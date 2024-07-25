from django.contrib import admin
from .models import Brand, Fuel, TransmissionType


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


class TransmissionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_transmission')
    list_display_links = ('id', 'name_transmission')
    search_fields = ('name_transmission',)
    list_per_page = 25


class FuelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_fuel')
    list_display_links = ('id', 'name_fuel')
    search_fields = ('name_fuel',)
    list_per_page = 25

'''
class PricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_pricing')
    list_display_links = ('id', 'name_pricing')
    search_fields = ('name_pricing',)
    list_per_page = 25
'''


admin.site.register(Brand, BrandAdmin)
admin.site.register(TransmissionType, TransmissionTypeAdmin)
admin.site.register(Fuel, FuelAdmin)

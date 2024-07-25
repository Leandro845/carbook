from celery import shared_task
from .models import Car
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from django.core.serializers import serialize

@shared_task
def make_a_trip_task(pick_up_location, pick_up_date, drop_off_date):
    # Convert string dates to datetime objects.
    pick_up_date = datetime.strptime(pick_up_date, '%Y-%m-%d')
    drop_off_date = datetime.strptime(drop_off_date, '%Y-%m-%d')

    # Make datetime objects timezone-aware.
    pick_up_date = timezone.make_aware(pick_up_date, timezone.get_current_timezone())
    drop_off_date = timezone.make_aware(drop_off_date, timezone.get_current_timezone())
    
    # Query for available cars that match the pick-up location and are available.
    # Exclude cars that overlap with the given pick-up and drop-off dates.
    available_cars = Car.objects.filter(
        location__name_city=pick_up_location,
        available=True,
    ).exclude(
        Q(pick_up_date__lte=pick_up_date, drop_off_date__gte=pick_up_date) |
        Q(pick_up_date__lte=drop_off_date, drop_off_date__gte=drop_off_date)
    )

    # Serialize the queryset to JSON format for further processing.
    return serialize('json', available_cars)

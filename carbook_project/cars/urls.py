from django.urls import path
from . import views


urlpatterns = [
    path('pricing/', views.pricing, name='pricing'),
    path('car-list/', views.car_list, name='car_list'),
    path('car-detail/<int:pk>/', views.car_detail, name='car_detail'),
    path('book-car/<int:pk>', views.book_car, name='book_car'),
    path('make-a-trip/', views.make_a_trip, name='make_a_trip'),
]
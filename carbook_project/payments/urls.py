from django.urls import path
from . import views


urlpatterns = [
    path('online-payment/<int:pk>', views.online_payment, name='online_payment'),
    path('payment/<int:pk>', views.payment, name='payment'),
    path("success/", views.success, name='success'),
    path('error/', views.error, name='error'),
    path('stripe_webhook', views.stripe_webhook, name="stripe_webhook"),
]
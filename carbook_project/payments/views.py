from django.shortcuts import render, get_object_or_404
from cars.models import Car
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def payment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    rent_type = request.GET.get('rent_type', 'day')
    price = request.GET.get('price')

    if not price:
        if rent_type == 'hour':
            price = car.pricing_per_hour
        elif rent_type == 'month':
            price = car.pricing_per_month
        else:
            price = car.pricing_per_day
    else:
        price = float(price)

    intent = stripe.PaymentIntent.create(
        amount=int(price * 100),
        currency='BRL',
        metadata={
            'car_id': car.id,
            'rent_type': rent_type,
            'price': price,
            'pickup_date': car.pick_up_date,
            'return_date': car.drop_off_date,
        }
    )

    return JsonResponse({
        'clientSecret': intent['client_secret']
    })


def online_payment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    rent_type = request.GET.get('rent_type', 'day')
    price = request.GET.get('price')

    if not price:
        if rent_type == 'hour':
            price = car.pricing_per_hour
        elif rent_type == 'month':
            price = car.pricing_per_month
        else:
            price = car.pricing_per_day
    else:
        price = float(price)

    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    context = {
        'car': car,
        'price': price,
        'rent_type': rent_type,
        'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY
    }
    return render(request, 'online_payment.html', context)


def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'payment_intent.succeeded':
        # Handle the successful payment here
        pass

    return HttpResponse(status=200)

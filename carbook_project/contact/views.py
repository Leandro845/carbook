from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    
    elif request.method == 'POST':
        name = request.POST.get('your_name')
        email = request.POST.get('your_email')
        subject = request.POST.get('your_subject')
        message = request.POST.get('your_message')

        if not all([name, email, subject, message]):
            messages.error(request, 'All fields are required')
            return redirect('contact')

        send = send_mail(
            subject,
            f'{name} - {message}',
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        try:
            send
            messages.success(request, 'Email sent successfully')
            return redirect('contact')
        except:
            messages.error(request, 'Email sent error')
            return redirect('contact')
        

from django.shortcuts import render
from . models import TrackingNumber
from django.contrib import messages

def index(request):
    return render(request, 'pages/base.html')


def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'pages/contact.html', {'title': 'Contact'})


def services(request):
    return render(request, 'pages/service.html', {'title': 'Contact'})


def track(request):
    return render(request, 'pages/track.html', {'title': 'Track'})


# Handle the track code from the form

def tracking(request):
    if request.method == 'POST':
        value = request.POST.get('track_value')
        if TrackingNumber.objects.filter(unique_id=value).exists():
            tracking_num = TrackingNumber.objects.get(unique_id=value)
            context = {'track_code': tracking_num}

            return render(request, 'pages/tracking-details.html', context)

        else:
            messages.warning(request, 'Invalid tracking number')
        return render(request, 'pages/404.html')  
    else:
        return render(request, 'pages/track.html') 
        

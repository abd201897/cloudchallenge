import json
import mimetypes
import os
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, JsonResponse
# Create your views here.
from django.views.generic.base import TemplateView
import requests

from weather_map import settings
from .apod import fetch_and_save_apod_image, fetch_and_mars_rover_image
from .models import MarsPhoto, APODImage
from decouple import config

class HomeView(TemplateView):

  template_name = 'weather/home.html'
  success_url = reverse_lazy('home')


def weather_view(request):

  if request.method == 'GET' and 'lat' in request.GET and 'lon' in request.GET:
    lat = request.GET['lat']
    lon = request.GET['lon']
    api_key = config('WEATHER_API_KEY', cast=str)
    units = 'metric'
    lang = 'fr'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}&lang={lang}'
    response = requests.get(url)
    
 
    if response.status_code == 200:
      data = response.json()
      return JsonResponse(data)
    else:
      return JsonResponse({'error': 'Unable to fetch weather data'}, status=500)
  else:
    return JsonResponse({'error': 'Invalid request method or missing coordinates'}, status=400)


# apod/views.py


def apod_image_view(request):
    #api_key = config('APOD_API_KEY', cast=str)
    api_key="fb3pI8MJ2FhwWQZRvRY3RWOoWigZbX6qWbWcChpI"
    apod_image = fetch_and_save_apod_image(api_key)
    return render(request, 'weather/apod.html', {'apod_image': apod_image})


def mars_rover_images_view(request):
    rover_camera = request.GET.get('camera')
    api_key = "fb3pI8MJ2FhwWQZRvRY3RWOoWigZbX6qWbWcChpI"
    photos = fetch_and_mars_rover_image(api_key, rover_camera)
    return render(request, 'weather/mars.html', {'photos': photos})

def nasa_api(request): 
    return render(request, 'weather/nasa.html')



def call_azure_function_view(request):
    azure_function_url = settings.AZURE_FUNCTION_URL

    try:
        response = requests.get(azure_function_url)
        response.raise_for_status()
        message = response.text
        return JsonResponse({'message': message})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def download_image(request, photo_id):
    try:
        mars_photo = MarsPhoto.objects.get(photo_id=photo_id)
    except MarsPhoto.DoesNotExist:
        raise Http404("Image not found.")
    
    with mars_photo.image.open('rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpg')
        response['Content-Disposition'] = f'attachment; filename="{mars_photo.image}"'
        return response
    

def send_email_view(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        #subject = "This is the test message"
        #body = "This is the test message"
        sender_email = config('EMAIL_HOST_USER', cast=str)
        sender_password = config('EMAIL_HOST_PASSWORD', cast=str)
 

        # Azure Function URL
        azure_function_url = settings.AZURE_FUNCTION_URL

        # Email parameters
        payload = {
                     "recipient": recipient,
                      "subject": "Test Subject",
                      "body": f"This is a test email that user {recipient} viewed images.",
                      "sender_email": sender_email,
                      "sender_password": sender_password
                  }

        # Send POST request to Azure Function
        response = requests.post(azure_function_url, json=payload)

        if response.status_code == 200:
            return redirect('nasa_api')
        else:
            return HttpResponse(f"Failed to send email: {response.text}", status=response.status_code)

    return render(request, 'weather/send_mail.html')


def download_apod(request, id):
    try:
        apod_photo = APODImage.objects.get(id=id)
        
    except APODImage.DoesNotExist:
        raise Http404("Image not found.")
    
    with apod_photo.image_file.open('rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpg')
        response['Content-Disposition'] = f'attachment; filename="{apod_photo.image_file}"'
        return response
    
    


    





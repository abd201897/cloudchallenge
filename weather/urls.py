from django.contrib import admin
from django.urls import path
from .views import HomeView, weather_view, apod_image_view, mars_rover_images_view, call_azure_function_view, download_image, send_email_view, download_apod


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('weather/', weather_view, name='weather_view'),
    path('apod/', apod_image_view, name='apod_image_view'),
    path('mars/', mars_rover_images_view, name='mars_rover_images_view'),
    path('test/', call_azure_function_view, name='call_azure_function_view'),
    path('download/<int:photo_id>', download_image, name='download_image'),
    path('send_email/', send_email_view, name='send'),
    path('download/<str:image>', download_apod, name='download_apod'),

    
]
# apod/utils.py
import requests
from django.core.files.base import ContentFile
from .models import APODImage, MarsPhoto
from django.conf import settings
from datetime import datetime

def fetch_and_save_apod_image(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and 'url' in data:
        image_url = data['url']
        response = requests.get(image_url)
        if response.status_code == 200:
            image_name = image_url.split("/")[-1]
            apod_image = APODImage(
                title=data['title'],
                date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
                explanation=data['explanation'],
                image_url=image_url
            )
            apod_image.image_file.save(image_name, ContentFile(response.content))
            apod_image.save()
            return apod_image
    return None


def fetch_and_mars_rover_image(api_key, rover_camera):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera={rover_camera}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        for photo in data['photos']:
            image_url = photo['img_src'] #fetch img_src from the json
            id = photo['id'] # fetch photo id from json
            image_name = image_url.split("/")[-1]
            if not MarsPhoto.objects.filter(photo_id = id).exists():
              apod_image = MarsPhoto(
                photo_id=id,
                img_src=image_url         
              )
              apod_image.image.save(image_name, ContentFile(response.content))
              apod_image.save()

        return data['photos']
    else:
        return None

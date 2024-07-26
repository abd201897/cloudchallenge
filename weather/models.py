from django.db import models

# Create your models here.

# apod/models.py
from django.db import models

class APODImage(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    explanation = models.TextField()
    image_url = models.URLField()
    image_file = models.ImageField(upload_to='apod_images/')

    def __str__(self):
        return self.title


class MarsPhoto(models.Model):
    photo_id = models.IntegerField(unique=True)
    img_src = models.URLField()
    image = models.ImageField(upload_to='downloads/', null=True, blank=True)
   

    def __str__(self):
        return f"Photo ID: {self.photo_id}"
    

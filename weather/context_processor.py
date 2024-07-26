  # your_app/context_processors.py

from django.conf import settings

def media_url(request):
    print(f'MEDIA_URL', settings.MEDIA_URL)
    return {'MEDIA_URL': settings.MEDIA_URL}

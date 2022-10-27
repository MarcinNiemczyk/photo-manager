import os
import requests
from django.conf import settings
from colorthief import ColorThief


def download_image(url):
    filename = url.split('/')[-1] + '.jpg'
    path = os.path.join(settings.MEDIA_ROOT, filename)
    image = requests.get(url).content
    with open(path, 'wb') as f:
        f.write(image)
    return filename


def get_dominant_color(filename):
    path = os.path.join(settings.MEDIA_ROOT, filename)
    image = ColorThief(path)
    dominant_color = image.get_color(quality=1)
    hex_code = f"#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}"
    return hex_code

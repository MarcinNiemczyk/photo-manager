import os
import requests
from colorthief import ColorThief
from django.conf import settings


def download_image(url):
    """Download image from given url and save it locally"""
    filename = url.split('/')[-1] + '.jpg'
    path = os.path.join(settings.MEDIA_ROOT, filename)
    image = requests.get(url).content
    with open(path, 'wb') as f:
        f.write(image)
    return filename


def get_dominant_color(filename):
    """Calculate image dominant color"""
    path = os.path.join(settings.MEDIA_ROOT, filename)
    image = ColorThief(path)
    dominant_color = image.get_color(quality=1)
    hex_code = f"#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}"
    return hex_code

import os
import requests
from django.conf import settings


def download_image(url):
    filename = url.split('/')[-1] + '.jpg'
    path = os.path.join(settings.MEDIA_ROOT, filename)
    image = requests.get(url).content
    with open(path, 'wb') as f:
        f.write(image)
    return filename

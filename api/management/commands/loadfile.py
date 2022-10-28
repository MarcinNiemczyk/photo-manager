import os
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from api.management.commands._private import store_data


class Command(BaseCommand):
    """Import photos from JSON file"""
    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        file = os.path.join(settings.BASE_DIR, options['filename'])
        with open(file, 'r') as f:
            data = f.read()
            data = json.loads(data)
        store_data(data)

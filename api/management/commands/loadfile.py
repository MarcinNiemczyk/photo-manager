from django.core.management.base import BaseCommand
import os
import json
from django.conf import settings
from ._private import store_data


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        file = os.path.join(settings.BASE_DIR, options['filename'])
        with open(file, 'r') as f:
            data = f.read()
            data = json.loads(data)
        store_data(data)

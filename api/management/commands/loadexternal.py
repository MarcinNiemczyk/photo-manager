import requests
from django.core.management.base import BaseCommand
from api.management.commands._private import store_data


class Command(BaseCommand):
    """Import photos from external API"""
    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        try:
            data = requests.get(options['url']).json()
        except requests.exceptions.JSONDecodeError:
            print('Content type must be JSON')
            return
        store_data(data)

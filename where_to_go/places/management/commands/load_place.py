from django.core.management.base import BaseCommand
from . import load_place


class Command(BaseCommand):
    help = 'Loading new place from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        path = options['path']
        load_place(path)

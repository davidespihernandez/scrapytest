from django.core.management.base import BaseCommand
from django.db import transaction

from news.media_reader import read_all_media


class Command(BaseCommand):
    help = 'Create media'

    @transaction.atomic
    def handle(self, *args, **options):
        self.launch()

    def launch(self):
        read_all_media()

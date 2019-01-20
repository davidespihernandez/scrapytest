from django.core.management.base import BaseCommand
from django.db import transaction
from news.models import Media


class Command(BaseCommand):
    help = 'Create media'

    @transaction.atomic
    def handle(self, *args, **options):
        self.create_data()

    def create_data(self):
        print("Creating media")
        default_media = [
            {
                "name": "El Mundo",
                "rule": "h2>a",
                "url": "https://www.elmundo.es/",
            },
            {
                "name": "El País",
                "rule": "h2>a",
                "url": "https://elpais.com/",
            },
            {
                "name": "ABC",
                "rule": "h3.titular>a",
                "url": "https://www.abc.es/",
            },
        ]

        for media in default_media:
            Media.objects.update_or_create(
                name=media.get("name"),
                defaults={
                    "title_rule": media.get("rule"),
                    "url": media.get("url"),
                },
            )

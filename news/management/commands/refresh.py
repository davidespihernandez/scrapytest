from django.core.management.base import BaseCommand
from django.db import transaction
from news.models import Media


class Command(BaseCommand):
    help = 'Create media'

    @transaction.atomic
    def handle(self, *args, **options):
        self.refresh()

    def refresh(self):
        print("Refreshing")
        default_media = [
            {
                "name": "El Mundo",
                "rule": "h2",
            },
            {
                "name": "El País",
                "rule": "h2",
            },
            {
                "name": "ABC",
                "rule": "h3.titular",
            },
        ]
        for media in default_media:
            Media.objects.update_or_create(
                name=media.get("name"),
                title_rule=media.get("rule"),
            )

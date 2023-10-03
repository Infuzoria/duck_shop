from django.core.management import BaseCommand
from catalog.models import Category
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        with open('data.json') as f:
            data = json.load(f)

        categories_for_create = []
        for row in data:
            categories_for_create.append(
                Category(pk=row['pk'], name=row['fields']['name'], description=row['fields']['description'])
            )

        Category.objects.bulk_create(categories_for_create)

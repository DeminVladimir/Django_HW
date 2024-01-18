from django.core.management.base import BaseCommand
from homeapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Product.objects.get(id=6)
        order.add_date = '2022-12-31'
        order.save()

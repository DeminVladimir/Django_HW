from django.core.management.base import BaseCommand
from homeapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.filter(id=4)
        products.delete()
        del products

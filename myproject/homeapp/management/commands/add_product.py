from django.core.management.base import BaseCommand
from homeapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product = Product(
            prod_name="Ремень",
            description="Ремень из натур. кожи",
            price=3000.00,
            quantity_of_prod=3,
            add_date=""
        )

        product.save()


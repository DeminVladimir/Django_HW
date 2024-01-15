from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    user_address = models.TextField()
    register_date = models.DateField()


class Product(models.Model):
    prod_name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField(max_length=6)
    quantity_of_prod = models.IntegerField()
    add_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return f'{self.prod_name}, {self.description}, {self.price}, {self.quantity_of_prod}, {self.add_date}'


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    check_summ = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField()


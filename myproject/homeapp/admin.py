from django.contrib import admin
from .models import User, Product, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone_number'
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'prod_name',
        'description',
        'price',
        'image',
        'add_date',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'order_date',
    ]


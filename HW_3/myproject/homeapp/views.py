from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
import datetime


# Create your views here.


def user(request):
    return HttpResponse('User page')


def product(request):
    return HttpResponse('Product page')


def order(request):
    return HttpResponse('Order page')


def order_7(request, user_id):
    orders_for_w = []
    orders_for_m = []
    orders_for_y = []
    orders = Order.objects.filter(user=user_id)
    for order in orders:
        date_now = datetime.date.today()
        ord_at = order.order_date
        days_from_ord = date_now - ord_at
        if days_from_ord.days < 7:
            orders_for_w.append(order.product.prod_name)
        elif days_from_ord.days < 30:
            orders_for_m.append(order.product.prod_name)
        else:
            orders_for_y.append(order.product.prod_name)
    return render(request, 'homeapp/index.html', {
        'order_7': ''.join(orders_for_w),
        'order_30': ''.join(orders_for_m),
        'order_365': ''.join(orders_for_y),
    })


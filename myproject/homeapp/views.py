from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def user(request):
    return HttpResponse('User page')


def product(request):
    return HttpResponse('Product page')


def order(request):
    return HttpResponse('Order page')

from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
]

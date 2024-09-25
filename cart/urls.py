# cart/urls.py
from django.urls import path, re_path
from .views import *

app_name = 'cart'  # Add this line

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]

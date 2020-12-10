from django.urls import path
from .views import get_products, set_products

urlpatterns = [
    path('get_products/', get_products),
    path('set_products/', set_products),
]

from django.urls import path
from .views import get_products, set_product

urlpatterns = [
    path('get_products/', get_products),
    path('set_products/', set_product),
]

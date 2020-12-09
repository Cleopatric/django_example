from django.contrib import admin
from .models import Product, ProductOwner

PER_PAGE = 10


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name', 'product_id', 'owner_id']
    list_display = ('product_name', 'product_id', 'owner_id')
    list_per_page = PER_PAGE


class ProductOwnerAdmin(admin.ModelAdmin):
    search_fields = ['owner_name', 'owner_id']
    list_display = ('owner_name', 'owner_id')
    list_per_page = PER_PAGE


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductOwner, ProductOwnerAdmin)

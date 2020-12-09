from django.db import models


class ProductOwner(models.Model):
    owner_name = models.CharField(max_length=20, default='', blank=True, null=True)
    owner_id = models.IntegerField()

    class Meta:
        db_table = 'product_owners'


class Product(models.Model):
    product_name = models.CharField(max_length=80, default='', blank=True, null=True)
    product_id = models.IntegerField()
    owner_id = models.IntegerField()

    class Meta:
        db_table = 'products'

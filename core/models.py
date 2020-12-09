from django.db import models


class ProductOwner(models.Model):
    owner_name = models.CharField(max_length=20, default='', blank=True, null=True)
    owner_id = models.IntegerField()

    def __str__(self):
        return f'{self.owner_name} - {self.owner_id}'


class Product(models.Model):
    product_name = models.CharField(max_length=80, default='', blank=True, null=True)
    product_id = models.IntegerField()
    owner_id = models.IntegerField()

    def __str__(self):
        return f'{self.product_name} - {self.product_id} - {self.owner_id}'

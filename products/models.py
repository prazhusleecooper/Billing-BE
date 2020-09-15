from django.db import models


class Product(models.Model):
    productName = models.CharField(max_length=50, blank=False, default='')
    productPrice = models.FloatField(blank=False, default=0.0)
    productTax = models.FloatField(blank=False, default=0.0)
    productCode = models.CharField(max_length=15, blank=False, default='', unique=True)

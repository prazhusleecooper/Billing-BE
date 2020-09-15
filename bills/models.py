from django.db import models


class Bill(models.Model):
    customer = models.TextField( blank=False, default=0)
    productsList = models.TextField(blank=False, default='')
    timeOfPurchase = models.CharField(max_length=50, blank=False, default='')
    grandTotal = models.IntegerField(blank=False, default=0)
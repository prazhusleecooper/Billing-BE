from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=50, blank=False, default='', unique=True)
    phone = models.CharField(max_length=15, blank=False, default='', unique=True)
    code = models.CharField(max_length=25, blank=False, default='', unique=True)
    address = models.CharField(max_length=100, blank=False, default='')

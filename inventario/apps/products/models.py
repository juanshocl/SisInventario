# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models

# Create your models here.

class phones(models.Model):
    PHONETYPES = (
        (1,'Fijo'),
        (2,'Movil'),
        (3,'Comercial'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=14)
    type = models.IntegerField(choices=PHONETYPES)

    def __str__(self):
        return self.id

class state(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name =  models.CharField(max_length=50)

    def __str__(self):
        return self.name

class category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField( max_length=50)
    
    def __str__(self):
        return self.description

class provider(models.Model):
    id = models.CharField(primary_key=True ,max_length=50)
    businessname = models.CharField(max_length=50)
    categoryProvider = models.ForeignKey(category, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=50)
    phonesProvider = models.ForeignKey(phones, on_delete=models.CASCADE, default=None)
    stateProvider = models.ForeignKey(state, on_delete=models.CASCADE, default=None)
    credit = models.BooleanField()
    amount = models.IntegerField()

class photos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thumbnail = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    bigsize = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

class warehouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descriptionWarehouse = models.CharField( max_length=50)
    MinimumStock  = models.IntegerField()

class products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productProvider = models.ForeignKey(provider, on_delete=models.CASCADE, default=None)
    description =  models.CharField(max_length=20)
    creationDate = models.DateField(auto_now=True, auto_now_add=False)
    lastUpate = models.DateField(auto_now=True, auto_now_add=False)
    buy_price = models.DecimalField(max_digits=5, decimal_places=2)
    sale_price = models.DecimalField( max_digits=5, decimal_places=2)
    categoryProduct = models.ForeignKey(category, on_delete=models.CASCADE, default=None)
    photos = models.ForeignKey(photos, on_delete=models.CASCADE, default=False)
    warehouseProduct = models.ForeignKey(warehouse, on_delete=models.CASCADE, default = None)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
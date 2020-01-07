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
        return self.number

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    businessname = models.CharField(max_length=50)
    categoryProvider = models.ForeignKey(category, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=50)
    phonesProvider = models.ForeignKey(phones, on_delete=models.CASCADE, default=None)
    stateProvider = models.ForeignKey(state, on_delete=models.CASCADE, default=None)
    credit = models.BooleanField()
    amount = models.IntegerField()

    def __str__(self):
        return self.businessname


class warehouses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descriptionWarehouse = models.CharField( max_length=50)
    #product = models.ManyToManyField(products)
    stock = models.IntegerField(default=0)
    MinimumStock  = models.IntegerField(default=0)
    address  = models.CharField(max_length=50, default=None)
    phones = models.ForeignKey(phones, on_delete=models.CASCADE, default=0)
    first_admin = models.CharField(max_length=50, default=None)
    lastName_admin = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.descriptionWarehouse

    def get_warehouseName(self):
        return self.first_admin+' '+self.lastName_admin
    get_warehouseName.short_description = 'Nombre'

class products(models.Model):
    id = models.CharField(primary_key=True, editable=True, max_length= 14)
    productProvider = models.ForeignKey(provider, on_delete=models.CASCADE, default=None)
    description =  models.CharField(max_length=20)
    creationDate = models.DateField(auto_now=True, auto_now_add=False)
    lastUpate = models.DateField(auto_now=True, auto_now_add=False)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField( max_digits=10, decimal_places=2)
    categoryProduct = models.ForeignKey(category, on_delete=models.CASCADE, default=None)
    #photos = models.ForeignKey(photos, on_delete=models.CASCADE, default=False)
    thumbnail = models.ImageField(upload_to='static/img/thumbnail', height_field=None, width_field=None, max_length=None, default=None, blank=True)
    bigsize = models.ImageField(upload_to='static/img/bigsize', height_field=None, width_field=None, max_length=None, default=None, blank=True)
    warehouseProduct = models.ManyToManyField(warehouses)
    isActive = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    

    def __str__(self):
        return self.description

    def get_warehouse(self):
        #return self.warehouseProduct.descriptionWarehouse
        return ', '.join([p.descriptionWarehouse for p in self.warehouseProduct.all()])
        # return "\n".join([p.products for p in self.product.all()])
    
    get_warehouse.short_description = 'Almacen' 



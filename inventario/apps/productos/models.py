# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models

# Create your models here.

class products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name =  models.CharField(max_length=20)
    quantity = models.IntegerField(max_length=None)
    buy_price = models.DecimalField(max_digits=5, decimal_places=2)
    sale_price = models.DecimalField( max_digits=5, decimal_places=2)
    categorie_id = models.CharField(max_length=50)
    #media_id
    date = models.DateField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.name

class category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField( max_length=50)
    
    def __str__(self):
        return self.description

    
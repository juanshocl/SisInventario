from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, CreateView, RedirectView
from apps.products.models import products
from django.urls import reverse_lazy
from apps.products.form import ProductForm
# Create your views here.


class HomeList(ListView):
     model = products
     template_name = 'home/home.html'

class CreateProduct(CreateView):
     model = products
     template_name = 'crud/create.html'
     form_class = ProductForm
     success_url = reverse_lazy('home')

class ListProducts(ListView):
     model  = products
     template_name = 'crud/listProduct.html'

class StatisticsProducts(ListView):
     model = products
     template_name = 'statistics/statistics.html'
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, CreateView, RedirectView
from apps.products.models import products
# Create your views here.


class HomeList(ListView):
     model = products
     loop_range = range (1,6)
     paginate_by = 2
     template_name = 'home/home.html'
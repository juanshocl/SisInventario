from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, CreateView, RedirectView
from apps.products.models import products, warehouses
from django.urls import reverse_lazy
from apps.products.form import ProductForm
# Create your views here.


class HomeList(ListView):
     model = products
     template_name = 'home/home.html'

class CreateProduct(CreateView):
     model = products
     template_name = 'crud/createProduct.html'
     form_class = ProductForm
     success_url = reverse_lazy('home')

class ListProducts(ListView):
     model  = products
     template_name = 'crud/listProduct.html'
     #stock  = warehouses.objects.filter(id=products.warehouseProduct)


     # def get_context_data(self, **kwargs):
     #      context = super(ListProducts,self).get_context_data(**kwargs)
     #      product = warehouse.objects.filter(products.id).order_by('id')
     #      data = []
     #      for escuela in product:
     #           dic = {
     #           'Id': escuela.Id,
     #           'Name' : escuela.Name,
     #           'Score': promedio,
     #           'ImageMD':escuela.ImageMD, 
     #           'ImageProfile':escuela.ImageProfile,
     #           'Address':escuela.Address,
     #           'State_Province':escuela.State_Province,
     #           'Phone':escuela.Phone, 
     #           'Type':escuela.Type,
     #           'Review':escuela.Review,
     #      }
     #           data.append(dic)

     #      context['data'] = data
     #      return context

class UpdateProducts(UpdateView):
     model = products
     template_name = 'crud/updateProduct.html'
     form_class = ProductForm
     success_url = reverse_lazy('home')

class StatisticsProducts(ListView):
     model = products
     template_name = 'statistics/statistics.html'
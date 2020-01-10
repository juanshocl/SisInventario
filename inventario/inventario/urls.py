"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.products.views import HomeList, CreateProduct, ListProducts, StatisticsProducts, UpdateProducts, test

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', HomeList.as_view(), name='home'),
    path('create/', CreateProduct.as_view(), name='create'),
    path('list/', ListProducts.as_view(), name='list'),
    path('update/', UpdateProducts.as_view(), name='update' ),
    path('statistics/', StatisticsProducts.as_view(), name='statistics'),
    path('test/', test.as_view(), name='test'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

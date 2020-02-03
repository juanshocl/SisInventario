from django.contrib import admin
from django.contrib.auth.models import User
from apps.products.models import products, provider, category, phones, state, warehouses, user, clients, details, sales


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','productProvider', 'description', 'creationDate', 'lastUpate', 'buy_price', 'sale_price', 'categoryProduct', 'get_warehouse', 'isActive')
    #fields = ('id','productProvider', 'description', 'buy_price', 'sale_price', 'categoryProduct', 'get_warehouse', 'isActive', 'stock')

    
admin.site.register(products, ProductsAdmin)

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id','businessname', 'categoryProvider', 'address', 'phonesProvider', 'stateProvider', 'credit', 'amount')
    fields = ('businessname', 'categoryProvider', 'address', 'phonesProvider', 'stateProvider', 'credit', 'amount')

admin.site.register(provider, ProviderAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','description')


admin.site.register(category, CategoryAdmin)

class PhonesAdmin(admin.ModelAdmin):
    list_display  = ('number', 'type')


admin.site.register(phones, PhonesAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(state, StateAdmin)

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('descriptionWarehouse', 'MinimumStock', 'stock', 'address', 'phones', 'get_warehouseName')

admin.site.register(warehouses, WarehouseAdmin)

class detailsAdmin(admin.ModelAdmin):
    list_display = ('id','product')

admin.site.register(details, detailsAdmin)

class userAdmin(admin.ModelAdmin):
    list_display = ('rut','name','last_name','type')
admin.site.register(user, userAdmin)

class clientsAdmin(admin.ModelAdmin):
    list_display = ('rut','name','last_name','phone')
admin.site.register(clients, clientsAdmin)

class salesAdmin(admin.ModelAdmin):
    list_display = ('id','seller','client','buyer_name','date','get_details','taxes','total')
admin.site.register(sales, salesAdmin)

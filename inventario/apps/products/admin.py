from django.contrib import admin
from django.contrib.auth.models import User
from apps.products.models import products, provider, category, phones, state, photos, warehouse


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','productProvider', 'description', 'creationDate', 'lastUpate', 'buy_price', 'sale_price', 'categoryProduct', 'warehouseProduct', 'isActive')
    fields = ('id','productProvider', 'description', 'buy_price', 'sale_price', 'categoryProduct', 'warehouseProduct', 'isActive')

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

class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'bigsize')

admin.site.register(photos, PhotosAdmin)

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('descriptionWarehouse', 'MinimumStock')

admin.site.register(warehouse, WarehouseAdmin)
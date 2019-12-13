from django.contrib import admin
from django.contrib.auth.models import User
from apps.products.models import products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'productProvider', 'description', 'creationDate', 'lastUpate', 'buy_price', 'sale_price', 'categoryProduct', 'photos', 'warehouseProduct', 'isActive')
   # list_filter = ('Name', 'State_Province', 'Type')
   # fields = ['Name', ('ImageMD', 'ImageProfile'), 'Address', 'State_Province', 'Phone', 'Type', 'Review']
    
    # def get_State(self, obj):
    #     return obj.State_Province.NameSP
    # get_State.short_description = 'Comuna'

    # def get_typeName(self, obj):
    #     return obj.Type.Description
    # #     return ', '.join([ Type.Description for Typedescription in self.Type.all()[:3] ])
    # # return ', '.join([ User.Email for User in self.User.all()[:3] ])
    # get_typeName.short_description = 'Tipo Establecimiento'

admin.site.register(products, ProductsAdmin)
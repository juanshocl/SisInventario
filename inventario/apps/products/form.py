from django import forms
from apps.products.models import products

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = products

        fields = [
            'id',
            'productProvider',
            'description',
            #'creationDate',
            #'lastUpate',
            'buy_price',
            'sale_price',
            'categoryProduct',
            #'photos',
            'warehouseProduct',
            'isActive',
            'stock',
        ]
        labels = {
            'id':'Codigo',
            'productProvider': 'Proveedor',
            'description': 'Nombre del producto',
            #'creationDate':'Creado el',
            #'lastUpate':'Ultima actualizacion',
            'buy_price':'Precio de compra',
            'sale_price':'Precio de ventas',
            'categoryProduct':'Categoria',
            #'photos':'Fotos',
            'warehouseProduct':'Ubicacion',
            'isActive':'Activo',
            'stock': 'Stock',

        }
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'productProvider': forms.Select(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'buy_price': forms.TextInput(attrs={'class':'form-control'}),
            'sale_price': forms.TextInput(attrs={'class':'form-control'}),
            'categoryProduct': forms.Select(attrs={'class':'form-control'}),
            'warehouseProduct': forms.SelectMultiple(attrs={'class':'form-control'}),
            #'photos': forms.TextInput(attrs={'class':'form-control'}),
            'photos': forms.TextInput(attrs={'class':'form-control'}),
            'isActive': forms.CheckboxInput(attrs={'required': True, 'class':'form-control'}),  
            'stock' : forms.TextInput(attrs={'required': True, 'class':'form-control'}),  
        }
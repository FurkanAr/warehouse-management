from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'quantity')
        labels = {
            "name": "",
            "category": "",
            "quantity": "",
        }
    
        widgets= {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "category": forms.Select(attrs={"class": "form-select", "placeholder":"Category"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder":"Quantity"}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'order_quantity')
        labels = {
            "product": "Product",
            "order_quantity": "Order Quantity",
        }
        widgets= {
            "product": forms.Select(attrs={"class": "form-select", "placeholder":"Product"}),
            "order_quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder":"Order Quantity"}),
        }
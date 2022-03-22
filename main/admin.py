from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','staff', 'order_quantity')
    list_filter = ('date',)
    search_fields = ('product', 'staff')

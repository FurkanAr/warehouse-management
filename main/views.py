from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from numpy import prod
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User

@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    products = Product.objects.all()
    items_count = products.count()
    employees_count = User.objects.all().count()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect("main-home")
    else:
        form = OrderForm()
    context = {
        'orders' : orders,
        'form' : form,
        'products': products,
        'orders_count' : orders_count,
        'items_count' : items_count,
        'employees_count' : employees_count,

    }
    return render(request, "main/index.html", context)

@login_required(login_url='user-login')
def staff(request):
    employees = User.objects.all()
    employees_count = employees.count()
    orders_count = orders_count = Order.objects.all().count()
    items_count = Product.objects.all().count()
    context = {
        'employees' : employees,
        'employees_count' : employees_count,
        'orders_count' : orders_count,
        'items_count' : items_count,
    }
    return render(request, "main/staff.html", context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    employees = User.objects.get(id=pk)
    context = {
        'employees' : employees,
    }
    return render(request, "main/staff_detail.html", context)

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    employees_count = User.objects.all().count()
    items_count = items.count()
    orders_count = Order.objects.all().count()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} was added successfully')
            return redirect("main-product")
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
        'items_count': items_count,
        'employees_count' : employees_count,
        'orders_count' : orders_count,
    }
    return render(request, "main/product.html", context)

@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("main-product")
    else:
        form = ProductForm(instance=item)
    context = {
        'form' : form,
    }
    return render(request, "main/product_update.html", context)

@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    item.delete()
    messages.success(request, ("Product Was Deleted Successfully!!!"))
    return redirect("main-product")

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    employees_count = User.objects.all().count()
    items_count = Product.objects.all().count()

    context = {
        'orders' : orders,
        'orders_count': orders_count,
        'employees_count' : employees_count,
        'items_count' : items_count,
    }
    return render(request, "main/order.html", context)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main-home"),
    path('staff/', views.staff, name="main-staff"),
    path('staff/detail<int:pk>', views.staff_detail, name="main-staff-detail"),
    path('product/', views.product, name="main-product"),
    path('product/delete/<int:pk>/', views.product_delete, name="main-product-delete"),
    path('product/update/<int:pk>/', views.product_update, name="main-product-update"),
    path('order/', views.order, name="main-order"),

]

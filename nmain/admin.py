from django.contrib import admin
from .models import *


@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'dummyP', 'category', 'offer', 'image']


@admin.register(cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email']


@admin.register(order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'date_ordered', 'quantity', 'status', 'transaction_id']


@admin.register(ShippingAddress)
class ShippingModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added']



# Register your models here.

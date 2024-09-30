from django.contrib import admin
from .models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'detail']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'count']


admin.site.register(CartModel, CartAdmin)
admin.site.register(CartItemModel, CartItemAdmin)

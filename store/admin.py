from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')
    search_fields = ('nome', 'email')
    list_filter = ('user',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital')
    list_filter = ('digital',)
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered', 'complete', 'transaction_id')
    list_filter = ('complete', 'date_ordered')
    search_fields = ('customer__name', 'tansaction_id')
    date_hierarchy = 'date_ordered'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('product__name', 'order__id')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added')
    list_filter = ('date_added', 'state')
    search_fields = ('customer__name', 'address', 'city', 'state', 'zipcode')
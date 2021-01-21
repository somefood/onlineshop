from django.contrib import admin
from .models import Order, OrderItem, OrderTransaction


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderTransaction)
class OrderTransactionAdmin(admin.ModelAdmin):
    pass
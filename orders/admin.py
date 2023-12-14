from django.contrib.admin import ModelAdmin, register

from orders.models import Order, OrderItem


@register(Order)
class OrderAdmin(ModelAdmin):
    """Custom order admin"""

    list_display = ["id", "order_number", "customer", "order_date", "address"]
    search_fields = ["id", "order_number", "customer", "order_date"]
    list_filter = ["id", "order_number", "customer", "order_date"]


@register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    """Custom orderItem admin"""

    list_display = ["id", "order", "product", "quantity"]
    search_fields = ["id", "order", "product"]
    list_filter = ["id", "order", "product"]

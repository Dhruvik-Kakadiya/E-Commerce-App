from django.contrib.admin import ModelAdmin, register

from products.models import Product


@register(Product)
class ProductAdmin(ModelAdmin):
    """Custom product admin"""

    list_display = ["id", "name", "weight"]
    search_fields = ["id", "name", "weight"]
    list_filter = ["id", "name", "weight"]

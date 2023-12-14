from django.contrib.admin import ModelAdmin, register

from customers.models import Customer


@register(Customer)
class CustomerAdmin(ModelAdmin):
    """Custom customer admin"""

    list_display = ["id", "name", "contact_number", "email"]
    search_fields = ["id", "name", "email"]
    list_filter = ["id", "name", "email"]

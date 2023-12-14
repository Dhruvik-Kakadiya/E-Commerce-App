from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # * If it's a new instance
        if not self.pk:
            last_order = Order.objects.all().order_by("-id").first()
            if last_order:
                # * Extract the number part
                last_order_number = int(last_order.order_number[3:])
                # * Increment by 1
                new_order_number = "ORD{:05d}".format(last_order_number + 1)
            else:
                # * For the first entry
                new_order_number = "ORD00001"
            self.order_number = new_order_number
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_number}_{self.customer.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order} - {self.product} - {self.quantity}"

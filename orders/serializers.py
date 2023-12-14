from datetime import datetime

from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    """ModelSerializer for OrderItem model"""

    class Meta:
        model = OrderItem
        fields = ("product", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateField(input_formats=["%d/%m/%Y"])
    order_number = serializers.CharField(read_only=True)
    order_item = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ("order_number", "customer", "order_date", "address", "order_item")

    def create(self, validated_data):
        order_items_data = validated_data.pop("order_item")

        # * Calculate order total weight
        total_weight = sum(
            item["product"].weight * item["quantity"] for item in order_items_data
        )

        # * Check if order total weight is not more then 150kg
        if total_weight > 150:
            raise serializers.ValidationError(
                "Order cumulative weight must be under 150kg."
            )

        # * Create order
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop("order_item", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if order_items_data is not None:
            # Handle update of OrderItems using the reverse relation 'order_items'
            instance.orderitem_set.all().delete()
            for item_data in order_items_data:
                OrderItem.objects.create(order=instance, **item_data)

        return instance

    def validate_order_date(self, value):
        from datetime import date

        if value < date.today():
            raise serializers.ValidationError("Order Date cannot be in the past.")
        return value

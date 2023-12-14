from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ModelSerializer for Product model"""

    class Meta:
        model = Product
        fields = "__all__"

    def validate_name(self, value):
        existing_product = Product.objects.filter(name=value).exists()
        if existing_product:
            raise serializers.ValidationError("Product name must be unique.")
        return value

    def validate_weight(self, value):
        if value <= 0 or value > 25:
            raise serializers.ValidationError(
                "Weight must be a positive decimal not more than 25kg."
            )
        return value

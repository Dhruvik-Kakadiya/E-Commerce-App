from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """ModelSerializer for Customer model"""

    class Meta:
        model = Customer
        fields = "__all__"

    def validate_name(self, value):
        existing_customer = Customer.objects.filter(name=value).exists()
        if existing_customer:
            raise serializers.ValidationError("Customer name must be unique.")
        return value

    def update(self, instance, validated_data):
        # * By setting partial=True, serializer only updates provided fields
        instance.name = validated_data.get('name', instance.name)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

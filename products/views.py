# products/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ecommerce_app.constants import KEY_MESSAGE, KEY_PAYLOAD
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(APIView):
    def get(self, request):
        """API to fetch all products"""

        # * Fetch all products
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={
                KEY_MESSAGE: "Products fetch successfully",
                KEY_PAYLOAD: serializer.data,
            },
        )

    def post(self, request):
        """API to create new product"""

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    KEY_MESSAGE: "Product created successfully",
                    KEY_PAYLOAD: serializer.data,
                },
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                KEY_MESSAGE: serializer.errors,
            },
        )

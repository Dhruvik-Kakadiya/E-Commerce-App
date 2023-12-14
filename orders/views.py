from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ecommerce_app.constants import KEY_MESSAGE, KEY_PAYLOAD
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateView(APIView):
    def get(self, request):
        """API to fetch orders with query param"""

        products = request.query_params.get("products")
        customer = request.query_params.get("customer")

        if products:
            products_list = products.split(",")
            orders = Order.objects.filter(
                orderitem__product__name__in=products_list
            ).distinct()
        elif customer:
            orders = Order.objects.filter(customer__name=customer)
        else:
            orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={
                KEY_MESSAGE: "Orders fetch successfully",
                KEY_PAYLOAD: serializer.data,
            },
        )

    def post(self, request):
        """API to create new order"""

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    KEY_MESSAGE: "Order created successfully",
                    KEY_PAYLOAD: serializer.data,
                },
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                KEY_MESSAGE: serializer.errors,
            },
        )

    def put(self, request, pk):
        """API to update exiting order"""

        try:
            # * Fetch order with id
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={KEY_MESSAGE: f"Given order id {pk} does not exist"},
            )

        serializer = OrderSerializer(order, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    KEY_MESSAGE: "Order details updated successfully",
                    KEY_PAYLOAD: serializer.data,
                },
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                KEY_MESSAGE: "Invalid data send",
                KEY_PAYLOAD: serializer.errors,
            },
        )

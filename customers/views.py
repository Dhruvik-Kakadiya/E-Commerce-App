from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ecommerce_app.constants import KEY_MESSAGE, KEY_PAYLOAD
from .models import Customer
from .serializers import CustomerSerializer


class CustomerListCreateView(APIView):
    def get(self, request):
        """API to fetch all customers"""

        # * Fetch all customers
        customers = Customer.objects.all()

        serializer = CustomerSerializer(customers, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={
                KEY_MESSAGE: "Customer list fetch successfully",
                KEY_PAYLOAD: serializer.data,
            },
        )

    def post(self, request):
        """API to create customer"""

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    KEY_MESSAGE: "Customer created successfully",
                    KEY_PAYLOAD: serializer.data,
                },
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                KEY_MESSAGE: serializer.errors,
            },
        )


class CustomerDetailView(APIView):
    def patch(self, request, pk):
        """API to update the existing customer"""

        try:
            # * Fetch customer with id
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={KEY_MESSAGE: f"Given customer id {pk} does not exist"},
            )

        serializer = CustomerSerializer(customer, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    KEY_MESSAGE: "Customer details updated successfully",
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

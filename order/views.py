from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from helpers.pagination import CustomPagination
from .models import Order
from .serializers import OrderSerializer


# Create your views here.

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

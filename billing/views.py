from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from helpers.pagination import CustomPagination
from .models import Billing
from .serializers import BillingSerializer


# Create your views here.

class BillingList(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    pagination_class = CustomPagination

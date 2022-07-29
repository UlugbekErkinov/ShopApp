from urllib import request
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from helpers.pagination import CustomPagination
from .models import Product, Comment, Category
from .serializers import ProductSerializer, CommentUserSerializer
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.vary import vary_on_headers

# Create your views here.


class ProductList(generics.ListAPIView):
    queryset = Product.objects.prefetch_related('comments','images').select_related('category')
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

class CommentUserList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUserSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)



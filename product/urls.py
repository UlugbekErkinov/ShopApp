from django.contrib import admin
from django.urls import path, include
from .views import ProductList, CommentUserList


urlpatterns = [
    path("product/", ProductList.as_view()),
    path("comment/", CommentUserList.as_view()),
    
   
]

from django.contrib import admin
from django.urls import path, include
from .views import OrderList


urlpatterns = [
    path("order/", OrderList.as_view()),
]

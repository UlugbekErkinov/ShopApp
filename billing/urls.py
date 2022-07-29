from django.contrib import admin
from django.urls import path, include
from .views import BillingList


urlpatterns = [
    path("billing/", BillingList.as_view()),
]

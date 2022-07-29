from django.db import models

# Create your models here.
from helpers.models import BaseModel
from common.models import User
from product.models import Product

STATUS_CHOICE = (
    ('Toshkent shahri', 'Toshkent shahri'),
    ('Andijon viloyati', 'Andijon viloyati'),
    ('Buxoro viloyati', 'Buxoro viloyati'),
    ('Jizzax viloyati', 'Jizzax viloyati'),
    ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'),
    ('Navoiy viloyati', 'Navoiy viloyati'),
    ('Namangan viloyati', 'Namangan viloyati'),
    ('Samarqand viloyati', 'Samarqand viloyati'),
    ('Surxondaryo viloyati', 'Surxondaryo viloyati'),
    ('Sirdaryo viloyati', 'Sirdaryo viloyati'),
    ('Toshkent viloyati', 'Toshkent viloyati'),
    ('Farg`ona viloyati', 'Farg`ona viloyati'),
    ('Xorazm viloyati', 'Xorazm viloyati'),
    ('Qoraqalpog`iston Respublikasi', 'Qoraqalpog`iston Respublikasi'),
)
BILLING_CHOICE = (
    ('Naqd', 'Naqd'),
    ('Karta', 'Orqali'),
    )

class Basket(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="nomi")
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()



class Billing(BaseModel):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    full_name = models.CharField(max_length=32, null=True, blank=True)
    region = models.CharField(max_length=32, choices=STATUS_CHOICE)
    address = models.TextField(max_length=256, blank=False, null=True)
    job_location = models.TextField(max_length=256, blank =False, null= True)
    note = models.TextField(max_length=256, blank=False, null=True)
    billing_method = models.CharField(max_length=32, choices=BILLING_CHOICE)

    
    
    






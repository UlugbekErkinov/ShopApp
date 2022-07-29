from django.db import models

# Create your models here.


from re import T
from django.db import models
from helpers.models import BaseModel
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import User
from product.models import Product

ORDER = (('yetqazib berildi','yetqazib berildi'),
          ('jarayonda', 'jarayonda'),
          ('bekor qilindi', 'bekor qilindi'))


class CartItem(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardItem = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    totalPrice = models.PositiveIntegerField()

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=ORDER)

    






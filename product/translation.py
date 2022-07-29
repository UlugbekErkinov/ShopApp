from modeltranslation.translator import translator, TranslationOptions
from .models import Product
from product.models import Product
from modeltranslation.forms import TranslationModelForm


from modeltranslation.translator import translator, TranslationOptions
from .models import Product


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Product, ProductTranslationOptions)

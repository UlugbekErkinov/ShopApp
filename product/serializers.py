from rest_framework import serializers
from product.models import Product, Category, ProductImage, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True)
    comments = CommentSerializer(many=True)
    

    class Meta:
        model = Product
        fields = ('category', 'images', 'comments')


class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"





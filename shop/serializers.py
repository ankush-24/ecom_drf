from rest_framework import serializers
from .models import Product,Cart,Order
from rest_framework import generics
from django.contrib.auth.models import User


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
from rest_framework import serializers
from .models import Product,Cart,Order
from rest_framework import generics
from django.contrib.auth.models import User


# class UserSerializers(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'product']

class UserSerializers(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = '__all__'

class ProductlistSerializers(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ['id','name']

class ProductdetailSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'

class ProductcreateSerializers(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'

# class ProductdestroySerializers(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Product
#         fields = '__all__'

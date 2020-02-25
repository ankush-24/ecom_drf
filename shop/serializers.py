from rest_framework import serializers
from .models import Product,Cart,Order
from rest_framework import generics
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'email','first_name','last_name']

# class UserSerializer(serializers.ModelSerializer):
#     # product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
#     # product = serializers.HyperlinkedRelatedField(many=True, view_name='ProductList', read_only=True)
#     class Meta:
#         model = User
#         fields = '__all__'

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

class ProductCreateSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'

class ProductUpdateSerializers(serializers.ModelSerializer):
    image = serializers.ImageField( use_url=True,required=False)
    class Meta:
        model = Product
        fields = '__all__'


# class UserUpdateSerializers(serializers.ModelSerializer):
#     # owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Product
#         fields = ['id','email']
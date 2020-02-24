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
    # product = serializers.HyperlinkedRelatedField(many=True, view_name='ProductList', read_only=True)
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
    # def get_profile_pic_url(self, obj):
    #     try:
    #         return self.context["request"].build_absolute_uri("/").strip("/")+str(obj.profile_pic.url)
    #     except Exception as E:
    #         print(E)
    #         return str("")            

# class ProductdestroySerializers(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Product
#         fields = '__all__'

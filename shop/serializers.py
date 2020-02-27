from rest_framework import serializers
from .models import Product,Cart,Order,Costumer
from rest_framework import generics
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'email','first_name','last_name']

class CostumerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Costumer
        fields= "__all__"

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


#PRICE VALIDATION
def PriceValidation(value):
    print('Price should be more then 5000')
    if value < 1000:
        raise serializers.ValidationError('Price should be more then 1000')

def NameValidation(value):
    print('Name mustn\'t contain any White space')
    var = ' '
    if var in value:
        raise serializers.ValidationError('Name mustn\'t contain any White space')

def DetailValidation(value):
    print('SHould only Contain 10 words')
    if len(value) < 10:
        raise serializers.ValidationError('SHould atleast only Contain 10 words')
    elif len(value) > 20:
        raise serializers.ValidationError('SHould Not Contain more then 20 words')        


class ProductCreateSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    price = serializers.IntegerField(validators=[PriceValidation,])
    name = serializers.CharField(validators=[NameValidation,])
    description = serializers.CharField(validators=[DetailValidation,])

    class Meta:
        model = Product
        fields = '__all__'

class ProductUpdateSerializers(serializers.ModelSerializer):
    image = serializers.ImageField( use_url=True,required=False)
    class Meta:
        model = Product
        fields = '__all__'





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email','first_name','last_name']


class UserProductSerializers(serializers.ModelSerializer):
    owner = UserSerializer(many=True)
    # costumer = CostumerSerializers(many=True)
    class Meta:
        model = Product
        fields = ['id','name','price','description','owner']

    def create(self, validated_data):
        owners_data = validated_data.pop('owner')
        product = Product.objects.create(**validated_data)
        for owner_data in owners_data:
            Costumer.objects.create(product, owner_data)


            



# class UserProductSerializers(serializers.ModelSerializer):
#    owner = serializers.ReadOnlyField(source='owner.id')
#    class Meta:
#         model =Product
#         fields = ('id','pname','owner')        
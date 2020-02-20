from django import forms
from .models import Product,Addcart,Order
from django.contrib.auth.models import User
class Productcreateforms(forms.ModelSerializer):
    class Meta:
        model=Product
        fields= "__all__"
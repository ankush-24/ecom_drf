from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Costumer(models.Model):
    c_name= models.CharField(max_length=100)
    c_age = models.IntegerField()
    c_address = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(max_length=1000)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', null=True, blank=True, related_name='product', on_delete=models.CASCADE)
    costumer = models.ForeignKey('Costumer', null=True, blank=True, related_name='product', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    orderitems = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    grandtotal = models.IntegerField(null=True, blank=True)
    user_address = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    subtotal = models.IntegerField(default=0)

    def __str__(self):
        return self.orderitems.name
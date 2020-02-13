from django.shortcuts import render
from rest_framework import viewsets
from shop.serializers import ProductSerializers,CartSerializers,OrderSerializers,UserSerializers
from shop.models import(Product,Cart,Order)
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User
from rest_framework import permissions
from shop.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


def home(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product})
# class home(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'

#     def get(self, request):
#         queryset = Product.objects.all()
#         return Response({'profiles': queryset})

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'product': reverse('productlist', request=request, format=format),
        # 'cart': reverse('cartlist', request=request, format=format),
        # 'order':reverse('orderlist',request=request,format=format),
        'user' : reverse('userlist',request=request,format=format),
    })

class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def get(self, request, format= None):
    #     return Response(serializer.data)
    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)    
	
    # def post(self, request, format=None):
    #     serializer = ProductSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = ProductSerializers(cart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializers(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CartList(APIView):
# 	def get(self, request, format= None):
# 		queryset = Cart.objects.all()
# 		serializer= CartSerializers(queryset, many=True)
# 		return Response(serializer.data)
# 	def post(self, request, format=None):
# 		serializer = CartSerializers(data=request.data)
# 		if serializer.is_valid():
# 		    serializer.save()
# 		    return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CartDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Cart.objects.get(pk=pk)
#         except Cart.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#         cart = self.get_object(pk)
#         serializer = CartSerializers(cart)
#         return Response(serializer.data)
#     def put(self, request, pk, format=None):
#         cart = self.get_object(pk)
#         serializer = CartSerializers(cart, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         cart = self.get_object(pk)
#         cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class OrderList(APIView):
# 	def get(self, request, format= None):
# 		queryset = Order.objects.all()
# 		serializer= OrderSerializers(queryset, many=True)
# 		return Response(serializer.data)
# 	def post(self, request, format=None):
# 		serializer = OrderSerializers(data=request.data)
# 		if serializer.is_valid():
# 		    serializer.save()
# 		    return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class OrderDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#         order = self.get_object(pk)
#         serializer = OrderSerializers(order)
#         return Response(serializer.data)
#     def put(self, request, pk, format=None):
#         order = self.get_object(pk)
#         serializer = OrderSerializers(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         order = self.get_object(pk)
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



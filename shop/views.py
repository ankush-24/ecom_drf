from django.shortcuts import render
from rest_framework import viewsets
from shop.serializers import CostumerSerializers,UserProductSerializers,ProductCreateSerializers,ProductlistSerializers,ProductdetailSerializers,ProductUpdateSerializers
from shop.models import(Product,Cart,Order,Costumer)
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
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from allauth.account.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.parsers import MultiPartParser, FormParser

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class Costumer(generics.ListCreateAPIView):
   queryset = Costumer.objects.all()
   serializer_class = CostumerSerializers

class UserProduct(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = UserProductSerializers


@csrf_exempt
@login_required
def home(request):
    user = request.user
    return render(request,'index.html',{'user':user})


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')  


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'product': reverse('productlist', request=request, format=format),
        'user' : reverse('userlist',request=request,format=format),
        # 'cart': reverse('cartlist', request=request, format=format),
        # 'order':reverse('orderlist',request=request,format=format),
    })

class ProductList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsAuthenticated]
    def get(self, request, format=None):
        # import pdb;pdb.set_trace()
        queryset = Product.objects.all()
        serializer= ProductlistSerializers(queryset, many=True)
        return Response(serializer.data)


class ProductDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()    
    # @method_decorator(login_required)
    def get(self, request, pk, format=None):
        user = self.get_object()
        serializer = ProductdetailSerializers(user)
        return Response(serializer.data)
        

# @method_decorator(login_required, name='dispatch')
class Productdestroy(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class= ProductlistSerializers
                
# @method_decorator(login_required, name='dispatch')
# class Productcreate(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class= ProductcreateSerializers
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.owner == request.user

class Productcreate(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]    
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers     
    def perform_create(self, serializer):
        # import pdb;pdb.set_trace();
        serializer.save(owner=self.request.user)

    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return obj.owner == request.user    


class ProductUpdate(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializers

    # parser_classes = (MultiPartParser, FormParser)
    # def get(self, request, pk, format=None):
    #     user = self.get_object()
    #     serializer = ProductUpdateSerializers(user)
    #     return Response(serializer.data)
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)  
# class Productcreate(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Product.objects.all()

#     serializer_class = ProductcreateSerializers

#     # def get(self, request, *args, **kwargs):
#     #     return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)    
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    # permission_classes = (IsAuthenticated,)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     try:
    #         return super(generics.CreateAPIView,self).create(request, *args, **kwargs)
    #     except IntegrityError:
    #         return bad_request(request)


    # def post(self, request, format=None):
    #     serializer = ProductcreateSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    # permission_classes = (IsAuthenticated,)
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
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



# class ProductDetail(APIView):
    
#     def get(self, request, pk, format=None):
#         snippet = Product.objects.get(pk=pk)
#         serializer = ProductSerializers(snippet)
#         return Response(serializer.data)


# def cart_detail(request,pk,format=None):
#     product = Product.objects.get(pk=pk)
#     product=product.id
#     return render(request,'cart_detail.html',{'product':product})

# class list(APIView):
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializers(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializers(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

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



# class UserList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class UserDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializers(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializers(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
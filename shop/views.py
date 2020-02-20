from django.shortcuts import render
from rest_framework import viewsets
from shop.serializers import ProductcreateSerializers,ProductlistSerializers,ProductdetailSerializers,UserSerializers
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
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

@csrf_exempt
def home(request):
    return render(request,'index.html')
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

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductlistSerializers



class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ProductdetailSerializers(user)
        return Response(serializer.data)


class Productdestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductlistSerializers
                

class Productcreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductcreateSerializers
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

class list(APIView):
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



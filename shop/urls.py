from django.urls import path
from shop import views

urlpatterns = [
    # path('', views.api_root),
    path('',views.home,name='home'),
    
    path('products/', views.ProductList.as_view(),name = 'productlist'),
    
    path('products/<int:pk>/', views.ProductDetail.as_view(),name = 'productdetail'),

    path('products/<int:pk>/destroy/', views.Productdestroy.as_view(),name = 'productdestroy'),

    path('create/', views.Productcreate.as_view(),name = 'productcreate'),    

    

    # path('cart_detail/<int:pk>/', views.cart_detail,name = 'cart_detail'),

 #    path('user/', views.UserList.as_view(),name= 'userlist'),

	# path('user/<int:pk>/', views.UserDetail.as_view()),

    # path('cart/', views.CartList.as_view(), name = 'cartlist'),
    # path('cart/<int:pk>/', views.CartDetail.as_view(), name = 'Cartdetail'),
    
    # path('order/', views.OrderList.as_view(), name= 'orderlist'),
    # path('order/<int:pk>/', views.OrderDetail.as_view(), name = 'orderdetail'),
    
    # path('user/', views.UserList.as_view(), name= 'userlist'),
    # path('user/<int:pk>/', views.UserDetail.as_view(), name = 'userdetail'),

]


"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'User', views.UserViewSet, basename = 'User')
# router.register(r'Product', views.ProductViewSet, basename = 'Product')
# router.register(r'Addcart', views.CartViewSet, basename = 'Addcart')
# router.register(r'Orders', views.OrderViewSet, basename = 'Orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

	
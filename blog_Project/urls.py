"""blog_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from blogAPI.views import MobileView
from productsapi.views import ProductView,ProductListView,ProductViewModelSerialView,ProductViewModelListView,ProductViewSetView,ProductModelViewSetView,UserRegistrationView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router_obj = DefaultRouter()  # used of viewset
router_obj.register("products/viewset",ProductViewSetView,basename="products") # don't put / at end
router_obj.register("products/modelviewset",ProductModelViewSetView,basename="mod")
router_obj.register("ecommerce/register",UserRegistrationView,basename="registration")
#When setting url make it different - i got value error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapi/mobile/',MobileView.as_view()),
    path('products/',ProductView.as_view()),
    path('products/<int:id>',ProductListView.as_view()),
    path('products/model/', ProductViewModelSerialView.as_view()),
    path('products/model/<int:id>', ProductViewModelListView.as_view()),
    path('accounts/token',obtain_auth_token),

]+router_obj.urls

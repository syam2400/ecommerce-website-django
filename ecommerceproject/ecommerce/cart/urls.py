"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from cart import views


app_name = 'cart'

urlpatterns = [
    path("add_to_cart/<int:p>/", views.add_to_cart, name='add_to_cart'),
    path('cartview', views.cartview, name='cartview'),
    path('cart_remove/<int:p>/', views.cart_remove, name='cart_remove'),
    path('full_remove/<int:k>/', views.full_remove, name='full_remove'),
    path('checkout', views.cart_checkout, name='checkout'),

    path("initiate_payment/", views.initiate_payment, name="initiate_payment"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment-failed/", views.payment_failed, name="payment_failed"),
  

]
# path('order_details',views.order_details,name='order_details'),
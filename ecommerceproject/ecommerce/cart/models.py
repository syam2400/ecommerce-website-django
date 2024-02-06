from django.db import models
from shop.models import Products
from django.contrib.auth.models import User



class Cart(models.Model):
    cart_products = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    data_added = models.DateField(auto_now_add=True)

    def subtotal(self):
        return self.quantity * self.cart_products.price

    def __str__(self):
        return self.cart_products.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    alternate_mobile_num = models.IntegerField(null=True,blank=True)
    order_status = models.CharField(max_length=30, default='pending',null=True,blank=True)
    delivery_status = models.CharField(max_length=30, default='pending',null=True,blank=True)
    no_of_items = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    ordered_products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.order.user.username
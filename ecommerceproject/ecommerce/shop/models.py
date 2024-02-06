from django.db import models



class Gender(models.Model):
    gen = models.CharField(max_length=130, unique=True)



    def __str__(self):
        return self.gen


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    gen = models.ForeignKey(Gender, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/category', null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/product-images', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Product_features(models.Model):
    item = models.ForeignKey(Products,on_delete=models.CASCADE)
    
    SIZE_CHOICES = [
        ('Small', 'S'),
        ('Medium', 'M'),
        ('Large', 'L'),
        ('Extra Large', 'XL'),
    ]
    item_size = models.CharField(max_length=30, choices=SIZE_CHOICES)
    COLOR_CHOICES = [
        ('black', 'black'),
        ('white', 'white'),
        ('red', 'red'),
        ('green', 'green'),
        ('blue', 'blue'),
        ('yellow', 'yellow'),
    ]
    item_color = models.CharField(max_length=50,choices=COLOR_CHOICES,)
    specific_item_image = models.ImageField(upload_to='shop/products', blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True,blank=True, null=True)

    def __str__(self):
     return self.item.name

 
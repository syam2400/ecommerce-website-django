from django.shortcuts import render, redirect
from shop.models import Category, Products, Gender ,Product_features
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomSignUpForm




def home(request):
    wom = Products.objects.filter(category__gen__gen='women')
    man = Products.objects.filter(category__gen__gen='man')
    kids = Products.objects.filter(category__gen__gen='kids')
    ac = Category.objects.get(slug='accessories')
    co = Category.objects.get(slug='cosmetics')
    acc = Products.objects.filter(category=ac)
    cos = Products.objects.filter(category=co)
    p = Products.objects.all()
    return render(request, 'index.html',
                  {'prod': p, 'women': wom, 'man': man, 'kids': kids, 'access': acc, "cosmetics": cos})


def all_products(request):
    p = Products.objects.all()[:len(Products.objects.all()) // 2]
    return render(request, 'product.html', {'p': p})

def all_products_page2(request):
    p = Products.objects.all()[len(Products.objects.all()) // 2:]
    return render(request, 'product_sec.html', {'p': p})

def pro_details(request,p=None,k=None):
    selected_item =None
    if k is not None:
         selected_item = Product_features.objects(COLOR_CHOICES=k)

    if p is not None:
       selected_product_details = Products.objects.get(slug=p)
    return render(request, 'details.html', {'selected_product_details': selected_product_details,'selected_item':selected_item})



# def sign_up(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         if(password1 != password2):
#             return ValueError('password mismatch')
#         else:
#              user = User.objects.create_user(email=email, password=password1)
#              user.save()
#              return redirect('shop:login')
#     else:    
#         return render(request,'signup.html')



def sign_up(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect or do something with the created user
            return redirect('shop:login')
    else:
        form = CustomSignUpForm()
    return render(request, 'signup.html', {'form': form})





def log_in(request):
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None :
            if user.is_staff:
              login(request, user)
              return home(request)
            else:
                login(request, user)
                return home(request)
        else:
            messages.error(request,'invalid credentials')
    return render(request, 'login.html')


@login_required
def profile_view(request):
    return render(request,'profile-view.html')


def user_logout(request):
    logout(request)
    return log_in(request)

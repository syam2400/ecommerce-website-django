from shop.models import Category
from shop.models import Gender
from cart.models import Cart
from django.contrib.auth.decorators import login_required


def menu_links(request):
    g = Gender.objects.all()
    c = Category.objects.all()
    return {'links': c, 'gender': g}


@login_required
def quantity(request):
    item_count = 0
    user = request.user
    k = Cart.objects.filter(user=user)
    for i in k:
        item_count += i.quantity
    return {'count': item_count}

def user_profile(request):
    user = request.user
    return {'user':user}


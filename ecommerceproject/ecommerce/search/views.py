from django.shortcuts import render
from shop.models import Products
from django.db.models import Q


def searchresults(request):
    query = ""
    products = None
    if (request.method == 'POST'):
        query = request.POST['q']
        print(query)
        if (query):
            products = Products.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'products': products, 'query': query})

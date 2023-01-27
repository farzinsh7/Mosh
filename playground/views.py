from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

def say_hello(request):
    queryset = Product.objects.all()[:5]
    

    return render(request, 'hello.html', {'name':'Farzin', 'products': list(queryset)})

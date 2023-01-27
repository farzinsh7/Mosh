from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer

def say_hello(request):
    queryset = Product.objects.filter(inventory__lt=10)
    

    return render(request, 'hello.html', {'name':'Farzin', 'products': list(queryset)})

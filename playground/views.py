from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, CartItem, Cart


def say_hello(request): 
    pass
    


    return render(request, 'hello.html', {'name':'Farzin'})

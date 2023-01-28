from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, CartItem, Cart


def say_hello(request): 
    item1 = Cart.objects.get(pk=3)
    item1.delete()
    


    return render(request, 'hello.html', {'name':'Farzin'})

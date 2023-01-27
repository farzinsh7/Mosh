from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

def say_hello(request):
    queryset = OrderItem.objects.filter(product__collection__id=3)
    

    return render(request, 'hello.html', {'name':'Farzin', 'products': list(queryset)})

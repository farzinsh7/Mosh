from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from store.models import Product,  Order, OrderItem, Customer

def say_hello(request):
    queryset = Customer.objects.annotate(orders_count=Count('order'))
    return render(request, 'hello.html', {'name':'Farzin', 'queryset': list(queryset)})

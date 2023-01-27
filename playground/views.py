from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product,  Order

def say_hello(request):
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'name':'Farzin', 'orders': list(queryset)})

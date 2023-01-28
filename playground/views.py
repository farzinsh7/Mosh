from django.shortcuts import render
from django.db.models import Value, F, ExpressionWrapper, DecimalField, Max, Count, Sum
from store.models import Product,  Order, Customer, Collection

def say_hello(request):
    queryset = Product.objects.annotate(total_sell = Sum(F('orderitem__unit_price') * F('orderitem__quantity'))).order_by('-total_sell')[:5]

    return render(request, 'hello.html', {'name':'Farzin', 'queryset': list(queryset)})

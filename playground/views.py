from django.shortcuts import render
from django.db.models.aggregates import Count, Min, Max
from store.models import Product,  Order

def say_hello(request):
    result =Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'))
    return render(request, 'hello.html', {'name':'Farzin', 'result': result})

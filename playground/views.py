from django.shortcuts import render
from django.db.models.aggregates import Count, Min, Max, Sum, Avg
from store.models import Product,  Order, OrderItem

def say_hello(request):
    result = Product.objects.filter(collection_id=3).aggregate(min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))
    return render(request, 'hello.html', {'name':'Farzin', 'result': result})

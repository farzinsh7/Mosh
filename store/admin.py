from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'collection_title', 'inventory_status']
    list_editable = ['unit_price']
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

    def collection_title(self,product):
        return product.collection.title

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            +'?'
            + urlencode({
                'customer_id': str(customer.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, customer.orders_count )
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count = Count('order'))


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'placed_at']
    

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({
                'collection_id': str(collection.id)
            }) 
            )
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

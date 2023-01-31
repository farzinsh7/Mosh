from django.contrib import admin
from . import models
from django.db.models import Count

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
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'placed_at']
    

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count
    

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

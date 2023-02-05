from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt = 10)
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'collection_title', 'inventory_status']
    list_editable = ['unit_price']
    list_select_related = ['collection']
    search_fields = ['title__istartswith']
    list_filter = ['collection', 'last_update', InventoryFilter]

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

    def collection_title(self,product):
        return product.collection.title

    
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count= queryset.update(inventory = 0)
        self.message_user(
            request, 
            f'{updated_count} products were successfully updated'
            )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


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


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'customer', 'placed_at']
    

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']

    
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

from django.contrib import admin

from stores.models import Store, Product, ProductBuy, ProductAdd


@admin.register(Store)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'count', 'created_at', 'updated_at', 'store', 'in_stock',
    )
    list_display_links = ('name',)
    list_filter = ('store',)
    search_fields = ('name', 'store__name',)
    save_on_top = True
    list_editable = ('in_stock',)


@admin.register(ProductBuy)
class ProductBuyAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'count', 'created_at', 'updated_at',)
    list_display_links = ('product',)
    list_filter = ('created_at', 'updated_at',)


@admin.register(ProductAdd)
class ProductAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'count', 'created_at', 'updated_at',)
    list_display_links = ('product',)
    list_filter = ('created_at', 'updated_at',)

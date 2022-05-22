from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'updated_at', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'barcode', 'brand', 'stocked', 'retail_price', 'wholesale_price',
                    'updated_at', 'created_at')
    list_filter = ('stocked', 'created_at',)
    search_fields = ('name', 'barcode', 'brand')
    ordering = ('name',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'image',
                    'updated_at', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__name',)
    ordering = ('created_at',)

from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category','status', 'created']
    list_filter = ['price','created', 'category','status']
    list_editable = ['price', 'quantity','category']
    readonly_fields = ('ttl_price',)

admin.site.register(Product, ProductAdmin)

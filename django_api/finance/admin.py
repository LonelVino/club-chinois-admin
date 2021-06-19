from django.contrib import admin

from .models import FinCategory, Finance


class FinCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(FinCategory, FinCategoryAdmin)


class FinanceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'buyer', 'description', 'created']
    list_filter = ['price','created', 'category']
    list_editable = ['name', 'price', 'buyer', 'category']
    readonly_fields = ('ttl_price',)

admin.site.register(Finance, FinanceAdmin)

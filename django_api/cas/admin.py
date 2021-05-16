from django.contrib import admin

from .models import Cas
# 内置的表
class OrderAdmin(admin.ModelAdmin):
    list_display = ['username','password','role']
    list_filter = ['created', 'updated']

admin.site.register(Cas)
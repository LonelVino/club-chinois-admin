'''
/django_api/views.py
-------------------------
Organize the views of Pages
'''

from django.shortcuts import render

from django.http import JsonResponse


def pages(request):
    return JsonResponse({'pages': ['User', 'Activity', 'Article']})

'''
/django_api/urls.py
-------------------------
Organize the api urls of parts: user, article, activity 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/', views.pages),
]
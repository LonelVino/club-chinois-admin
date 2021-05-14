'''
/django_api/urls.py
-------------------------
Organize the api urls of parts: user, cas, ane, vol, pitch 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/', views.pages),
]
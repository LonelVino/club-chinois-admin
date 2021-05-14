'''
/django_api/users/urls.py
-------------------------
Organize the api urls of User 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/ane_name', views.ane_name),
    path('/ane_info', views.ane_info),
]
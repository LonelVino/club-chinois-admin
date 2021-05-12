'''
/django_api/users/urls.py
-------------------------
Organize the api urls of User 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/activity_name', views.activity_name),
    path('/activity_info', views.activity_info),
]
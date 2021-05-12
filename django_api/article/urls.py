'''
/django_api/users/urls.py
-------------------------
Organize the api urls of User 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/article_name', views.article_name),
    path('/article_content', views.article_content),
]
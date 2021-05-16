'''
/django_api/vol/urls.py
-------------------------
Organize the api urls of Volant 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/all_scores', views.all_scores),
    path('/add_score', views.add_score),
]
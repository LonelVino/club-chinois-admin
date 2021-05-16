'''
/django_api/pitch/urls.py
-------------------------
Organize the api urls of Pitch 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('all_scores', views.all_scores),
    path('add_score', views.add_score),
]
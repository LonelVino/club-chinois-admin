'''
/django_api/users/urls.py
-------------------------
Organize the api urls of User 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('all_scores', views.all_scores),
    path('one_score', views.one_score),
    path('add_score', views.add_score),
    path('update_score', views.update_score),
    path('delete_score', views.a_score_delete_byId),
]
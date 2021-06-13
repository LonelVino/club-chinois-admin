'''
/django_api/pitch/urls.py
-------------------------
Organize the api urls of Pitch 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('all_scores', views.all_scores),
    path('one_score', views.one_score),
    path('add_score', views.add_score),
    path('update_score', views.update_score),
    path('del_score', views.p_score_delete_byId),
]
'''
/django_api/vol/urls.py
-------------------------
Organize the api urls of Volant 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('all_scores', views.all_scores),
    path('one_score', views.one_score),
    path('add_score', views.add_score),
    path('update_score', views.update_score),
    path('del_score', views.v_score_delete_byId),

    path('test_add_score', views.test_add_score),
]
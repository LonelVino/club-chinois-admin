'''
/django_api/users/urls.py
-------------------------
Organize the api urls of User 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/one_name', views.user_name),
    path('/one_info', views.user_info),
    path('/all_names', views.all_user_names),
    path('/all_infos', views.all_user_infos),

    path('/delete_by_id', views.user_delete_byId),

    path('/test_add', views.test_add),    
]
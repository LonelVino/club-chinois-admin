'''
/django_api/users/urls.py
-------------------------
Organize the api urls of User 
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.registry),
    path('/login', views.login),
    path('/logout', views.logout),

    path('/get_role', views.get_role),
    path('/getall', views.get_all_cas),

]
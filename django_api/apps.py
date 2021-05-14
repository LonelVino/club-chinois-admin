'''
/django_api/apps.py
-------------------------
Entrance of the Page(root: user, cas, ane, vol, pitch)
'''

from django.apps import AppConfig


class ApiExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_api'

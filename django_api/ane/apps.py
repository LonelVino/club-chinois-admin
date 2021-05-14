'''
/django_api/ane/apps.py
-------------------------
Entrance of the Ane
'''

from django.apps import AppConfig


class AneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ane'

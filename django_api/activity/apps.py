'''
/django_api/activity/apps.py
-------------------------
Entrance of the Activity
'''

from django.apps import AppConfig


class ActivityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activity'

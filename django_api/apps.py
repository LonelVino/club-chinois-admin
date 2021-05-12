'''
/django_api/apps.py
-------------------------
Entrance of the Page(root: user, article, activity)
'''

from django.apps import AppConfig


class ApiExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_api'

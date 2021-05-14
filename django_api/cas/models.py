'''
/django_api/Cas/models.py
-------------------------
Model of Cas
'''

from django.db import models
from django.utils import timezone


# Cas model
class Cas(models.Model):
    # Account
    username = models.CharField(max_length=100)
    # PWD
    password = models.TextField()
    # Role
    role = models.CharField(max_length=20,  default='editor')
    # role = ArrayField(ArrayField(models.CharField()))
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Cas'

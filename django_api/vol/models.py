'''
/django_api/user/vol/models.py
-------------------------
Model of Vol
'''

from django.db import models
from django.utils import timezone

# Ane model
class Vol(models.Model):
    # Name of ane
    user_id = models.IntegerField()
    # if the user finished the game,  - unfinished,  otherwise
    number = models.IntegerField(default=0)
    # The time used to finish the game, unfinished -> 0
    time = models.IntegerField(default=0)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Vol'
'''
/django_api/user/actvity.py
-------------------------
Model of Ane
'''

from django.db import models
from django.utils import timezone

# Ane model
class Ane(models.Model):
    # Name of ane
    name = models.CharField(max_length=100)
    # if the user finished the game,  - unfinished,  otherwise
    isFIni = models.BooleanField(default=0)
    # The time used to finish the game, unfinished -> 0
    time = models.IntegerField(default=0)
    # The score of this user
    a_score = models.IntegerField(default=0)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Ane'
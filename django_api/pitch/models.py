'''
/django_api/user/pitch/models.py
-------------------------
Model of Pitch
'''

from django.db import models
from django.utils import timezone

# Ane model
class Pitch(models.Model):
    # Name of ane
    name = models.CharField(max_length=100)
    # if the user finished the game,  - unfinished,  otherwise
    number = models.IntegerField(default=0)
    # The time used to finish the game, unfinished -> 0
    time = models.IntegerField(default=0)
    # The score of this user
    p_score = models.IntegerField(default=0)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Pitch'
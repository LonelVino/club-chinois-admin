'''
/django_api/user/actvity.py
-------------------------
Model of Ane
'''

from django.db import models
from django.utils import timezone
from django_api.user.models import User

# Ane model
class Ane(models.Model):
    # Name of ane
    name = models.CharField(max_length=100)
    # if the user take part in the game,  0 - not, 1 otherwise
    isPart = models.BooleanField(default=0)
    # if the user has the hint?,  0 - unfinished, 1  otherwise
    hasInd = models.BooleanField(default=0)
    # if the user finished the game,  0 - unfinished, 1  otherwise
    isFini = models.BooleanField(default=0)
    # if the user is freezed,  0 - unfreezed, 1  otherwise
    isFreeze = models.BooleanField(default=0)
    # The time used to finish the game, unfinished -> 0
    time = models.IntegerField(default=0)
    # The step user achieved
    step = models.IntegerField(default=0)
    # The score of this user
    a_score = models.IntegerField(default=0)
    # The comment of this user
    comment = models.TextField(default='None')
    # Begin time
    start_time = models.DateTimeField(default=timezone.now)
    # End time
    end_time = models.DateTimeField(default=timezone.now)
    # isStart - 1, isStop - 2, isEnd - 3 (default - 0)
    status = models.IntegerField(default=0)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0, related_name='anes')

    class Meta:
        db_table = 'Ane'
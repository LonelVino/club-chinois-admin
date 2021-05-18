'''
/django_api/user/vol/models.py
-------------------------
Model of Vol
'''

from django.db import models
from django.utils import timezone
from django_api.user.models import User

# Ane model
class Vol(models.Model):

    # Name of ane
    name = models.CharField(max_length=100)
    # if the user take part in the game,  0 - not, 1 otherwise
    isPart = models.BooleanField(default=0)
    # if the user is freezed,  0 - unfreezed, 1  otherwise
    isFreeze = models.BooleanField(default=0)
    # The number of users played with the volant
    number = models.IntegerField(default=0)
    # The time used to finish the game, unfinished -> 0
    time = models.IntegerField(default=0)
    # The score of this user
    v_score = models.IntegerField(default=0)
    # The comment of this user
    comment = models.TextField(default='None')
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0, related_name='vols')

    class Meta:
        db_table = 'Vol'
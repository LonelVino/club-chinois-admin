'''
/django_api/user/pitch/models.py
-------------------------
Model of Pitch
'''

from django.db import models
from django.utils import timezone
from django_api.user.models import User

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
    # The comment of this user
    comment = models.TextField(default='None')
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,  default=0, related_name='pitchs')

    class Meta:
        db_table = 'Pitch'
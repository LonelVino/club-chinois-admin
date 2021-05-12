'''
/django_api/user/actvity.py
-------------------------
Model of Activity
'''

from django.db import models
from django.utils import timezone

# Activity model
class Activity(models.Model):
    # Name of actvity
    act_name = models.CharField(max_length=100)
    # Location of the activity
    act_loc = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
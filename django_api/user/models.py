'''
/django_api/user/models.py
-------------------------
Model of User
'''

from django.db import models
from django.utils import timezone
# from django.contrib.postgres.fields import ArrayField

# User model
class User(models.Model):
    # Name
    name = models.CharField(max_length=100)
    # isAne  是否玩过Ane0rouge
    isAne = models.IntegerField()
    # "isVol": 0, //是否玩过volant
    isVol = models.IntegerField()
    # "isPitch": 0, //是否玩过投壶
    isPitch = models.IntegerField()
    # Email
    email = models.TextField()
    # Telephone
    telephone = models.TextField()      
    # Score
    score = models.IntegerField()  
    # Location of the Logement
    loc = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'User'

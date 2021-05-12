'''
/django_api/user/models.py
-------------------------
Model of User
'''

from django.db import models
from django.utils import timezone

# User model
class User(models.Model):
    # Name
    user_name = models.CharField(max_length=100)
    # Last Name
    last_name = models.CharField(max_length=100)
    # Email
    email = models.TextField()
    # Telephone
    telephone = models.TextField()      
    # Score
    score = models.IntegerField()  
    # Location of the Logement
    user_loc = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
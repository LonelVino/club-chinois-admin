from django.contrib import admin
from django_api.user import models as user_models
from django_api.cas import models as cas_models

# Register your models here.
admin.site.register(user_models.User)
admin.site.register(cas_models.Cas)
from django.contrib import admin
from django_api.user import models as user_models
from django_api.cas import models as cas_models
from django_api.ane import models as ane_models
from django_api.pitch import models as pitch_models
from django_api.vol import models as vol_models

# Register your models here.
admin.site.register(user_models.User)
admin.site.register(cas_models.Cas)
admin.site.register(ane_models.Ane)
admin.site.register(vol_models.Vol)
admin.site.register(pitch_models.Pitch)

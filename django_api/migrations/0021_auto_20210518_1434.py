# Generated by Django 3.2 on 2021-05-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0020_auto_20210518_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='ane',
            name='hasInd',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='ane',
            name='step',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2 on 2021-05-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0016_auto_20210518_0342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vol',
            name='number',
        ),
        migrations.AddField(
            model_name='ane',
            name='isPart',
            field=models.BooleanField(default=0),
        ),
    ]
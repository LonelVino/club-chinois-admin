# Generated by Django 3.2 on 2021-05-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0010_pitch_vol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ane',
            old_name='isFIni',
            new_name='isFini',
        ),
        migrations.RemoveField(
            model_name='ane',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='pitch',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='vol',
            name='user_id',
        ),
        migrations.AddField(
            model_name='ane',
            name='a_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ane',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pitch',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pitch',
            name='p_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vol',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vol',
            name='v_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cas',
            name='username',
            field=models.CharField(default='None', max_length=100),
        ),
    ]

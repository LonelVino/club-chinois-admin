# Generated by Django 3.2 on 2021-06-13 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0025_pitch_isfreeze'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='食品', max_length=200)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'Category',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='products/%Y/%m/%d')),
                ('quantity', models.IntegerField(default=0, max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('price', models.FloatField()),
                ('dt_info', models.CharField(default='None', max_length=200)),
                ('status', models.IntegerField(default=0, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default='食品', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='django_api.category')),
            ],
            options={
                'db_table': 'Product',
                'ordering': ('name',),
                'index_together': {('id',)},
            },
        ),
    ]

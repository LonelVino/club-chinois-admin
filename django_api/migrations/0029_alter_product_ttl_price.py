# Generated by Django 3.2 on 2021-06-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0028_product_ttl_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ttl_price',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

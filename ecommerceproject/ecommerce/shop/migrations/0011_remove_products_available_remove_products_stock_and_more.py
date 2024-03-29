# Generated by Django 4.2.5 on 2023-11-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_image_product_features_specific_item_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='available',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
        migrations.AddField(
            model_name='product_features',
            name='available',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='product_features',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

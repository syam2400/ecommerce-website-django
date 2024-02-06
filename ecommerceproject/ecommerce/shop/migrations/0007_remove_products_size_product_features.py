# Generated by Django 4.2.5 on 2023-11-19 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_products_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='size',
        ),
        migrations.CreateModel(
            name='Product_features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_size', models.CharField(choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('Extra Large', 'XL')], max_length=30)),
                ('item_color', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('red', 'red'), ('green', 'green'), ('blue', 'blue'), ('yellow', 'yellow')], max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
        ),
    ]

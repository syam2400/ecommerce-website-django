# Generated by Django 4.2.3 on 2023-10-01 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gender',
            old_name='kids',
            new_name='gen',
        ),
        migrations.RemoveField(
            model_name='gender',
            name='man',
        ),
        migrations.RemoveField(
            model_name='gender',
            name='woman',
        ),
    ]
# Generated by Django 3.2.10 on 2022-02-15 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_auto_20220215_0016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]

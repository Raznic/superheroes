# Generated by Django 2.1.4 on 2018-12-16 15:26

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('characters', '0002_auto_20181215_1616'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='SecretIdentity',
        ),
    ]

# Generated by Django 3.2 on 2021-06-26 22:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MonitoringService', '0002_alter_tender_hash'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserStat',
            new_name='UserStats',
        ),
    ]

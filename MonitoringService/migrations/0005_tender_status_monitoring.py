# Generated by Django 3.2 on 2021-07-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonitoringService', '0004_tender_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='status_monitoring',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 3.2 on 2021-07-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonitoringService', '0005_tender_status_monitoring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='status_monitoring',
            field=models.BooleanField(),
        ),
    ]

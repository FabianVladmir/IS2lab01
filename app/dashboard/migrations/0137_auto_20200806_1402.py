# Generated by Django 2.2.4 on 2020-08-06 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0136_auto_20200804_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ignore_tribes',
            field=models.ManyToManyField(blank=True, related_name='ignore', to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='tribessubscription',
            name='expires_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 6, 14, 2, 38, 236251, tzinfo=utc), null=True),
        ),
    ]
# Generated by Django 2.2.3 on 2019-10-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0014_questpointaward_round_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='override_background',
            field=models.CharField(default='', max_length=100),
        ),
    ]

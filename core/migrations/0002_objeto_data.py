# Generated by Django 3.0.5 on 2020-04-13 21:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objeto',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 4, 13, 21, 43, 50, 489838, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

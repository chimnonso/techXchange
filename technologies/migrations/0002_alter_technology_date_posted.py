# Generated by Django 3.2.8 on 2021-10-26 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Posted'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0004_remove_contact_date_requested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
    ]

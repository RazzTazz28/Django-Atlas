# Generated by Django 3.2.13 on 2022-04-15 23:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 0, 38, 56, 857732)),
        ),
    ]

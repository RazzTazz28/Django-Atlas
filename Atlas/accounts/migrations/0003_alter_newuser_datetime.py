# Generated by Django 3.2 on 2022-04-16 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_newuser_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 22, 11, 15, 670323)),
        ),
    ]

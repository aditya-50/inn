# Generated by Django 3.1.4 on 2021-02-25 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0010_auto_20210225_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
# Generated by Django 3.1.4 on 2021-02-14 09:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20210213_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.1.4 on 2021-02-13 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20210212_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posted_time',
            new_name='time',
        ),
    ]
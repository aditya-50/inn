# Generated by Django 3.1.4 on 2021-03-20 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0021_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='last_follow',
        ),
    ]

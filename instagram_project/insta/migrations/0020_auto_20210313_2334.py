# Generated by Django 3.1.4 on 2021-03-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0019_auto_20210307_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='text',
            field=models.CharField(default='', max_length=10000000),
        ),
    ]

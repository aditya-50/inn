# Generated by Django 3.1.4 on 2021-02-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

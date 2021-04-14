# Generated by Django 3.1.4 on 2021-04-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0026_customuser_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
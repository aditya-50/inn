# Generated by Django 3.1.4 on 2021-02-25 07:13

from django.db import migrations, models
import insta.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0013_auto_20210225_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='display_picture',
            field=models.ImageField(default='user.png', upload_to=insta.models.user_directory_path),
        ),
    ]
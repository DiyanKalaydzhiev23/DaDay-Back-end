# Generated by Django 4.0.3 on 2022-04-27 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_alter_profile_last_sent_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='parent_email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_sent_email',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 16, 18, 5, 137974)),
        ),
    ]

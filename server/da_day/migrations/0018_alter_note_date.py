# Generated by Django 4.0.3 on 2022-05-03 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da_day', '0017_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 18, 57, 59, 81445)),
        ),
    ]
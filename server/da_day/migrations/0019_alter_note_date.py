# Generated by Django 4.0.3 on 2022-05-09 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da_day', '0018_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 16, 57, 3, 980803)),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-30 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBox', '0002_alter_message_message_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.TimeField(default=datetime.datetime(2023, 1, 30, 21, 56, 46, 821138)),
        ),
    ]
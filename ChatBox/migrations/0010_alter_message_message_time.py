# Generated by Django 4.1.5 on 2023-02-04 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBox', '0009_alter_message_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 4, 9, 10, 35, 993288)),
        ),
    ]

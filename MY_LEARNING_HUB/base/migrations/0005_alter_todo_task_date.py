# Generated by Django 5.0.1 on 2024-02-25 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_todo_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 0, 6, 35, 802974, tzinfo=datetime.timezone.utc)),
        ),
    ]
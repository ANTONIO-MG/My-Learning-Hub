# Generated by Django 5.0.1 on 2024-02-25 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_todo_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 25, 0, 8, 59, 980156, tzinfo=datetime.timezone.utc)),
        ),
    ]

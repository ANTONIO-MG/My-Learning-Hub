# Generated by Django 5.0.1 on 2024-02-25 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_todo_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='todo',
            name='task_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 25, 0, 26, 14, 115138, tzinfo=datetime.timezone.utc)),
        ),
    ]
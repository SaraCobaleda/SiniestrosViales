# Generated by Django 4.1 on 2023-07-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0002_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]

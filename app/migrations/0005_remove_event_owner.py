# Generated by Django 4.2.10 on 2024-02-15 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_event_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="owner",
        ),
    ]

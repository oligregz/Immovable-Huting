# Generated by Django 4.1.3 on 2022-11-28 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("immovablehutting", "0006_alter_immoble_date_time_create"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="immoble",
            name="immoble_code",
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("immovablehutting", "0003_alter_immoble_immoble_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="immoble",
            name="immoble_code",
            field=models.BigIntegerField(max_length=10),
        ),
    ]

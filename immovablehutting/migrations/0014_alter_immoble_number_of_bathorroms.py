# Generated by Django 4.1.3 on 2022-11-29 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("immovablehutting", "0013_alter_immoble_guest_limit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="immoble",
            name="number_of_bathorroms",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
    ]
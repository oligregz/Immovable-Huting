# Generated by Django 4.1.3 on 2022-11-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("immovablehutting", "0015_alter_immoble_cleaning_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="annoucement",
            name="plataform_rate",
            field=models.FloatField(
                blank=True,
                help_text="digite a taxa da plataforma. ex: 13.00",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="annoucement",
            name="publishing_plataform",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="reserve",
            name="comment_field",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="reserve",
            name="number_of_guests",
            field=models.IntegerField(
                blank=True,
                choices=[
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5", "5"),
                    ("6", "6"),
                ],
                max_length=1,
                null=True,
            ),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-26 18:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="deck",
            name="time_created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="deck",
            name="deck_name",
            field=models.CharField(help_text="Enter name of deck", max_length=100),
        ),
        migrations.AlterField(
            model_name="deck",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Give a description for this deck...",
                max_length=200,
            ),
        ),
    ]

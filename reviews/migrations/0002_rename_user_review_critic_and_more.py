# Generated by Django 4.1 on 2022-08-20 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="user",
            new_name="critic",
        ),
        migrations.RenameField(
            model_name="review",
            old_name="movie",
            new_name="movie_id",
        ),
    ]
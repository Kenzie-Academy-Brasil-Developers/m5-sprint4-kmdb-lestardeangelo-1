# Generated by Django 4.1 on 2022-08-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_email_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
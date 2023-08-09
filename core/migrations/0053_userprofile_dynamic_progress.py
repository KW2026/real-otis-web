# Generated by Django 4.1.10 on 2023-08-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0052_alter_userprofile_last_notif_dismiss"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="dynamic_progress",
            field=models.BooleanField(
                default=False,
                help_text="Level meters show progression towards the next value to level up rather than a fixed max value",
                verbose_name="Dynamic level meters progression",
            ),
        ),
    ]

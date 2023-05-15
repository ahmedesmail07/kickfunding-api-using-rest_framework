# Generated by Django 4.2 on 2023-05-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_project_current_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="thumbnail",
            name="image_url",
        ),
        migrations.AddField(
            model_name="thumbnail",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="static/images"),
        ),
    ]

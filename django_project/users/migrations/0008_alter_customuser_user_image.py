# Generated by Django 4.2 on 2023-05-13 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_alter_customuser_birth_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_image",
            field=models.FileField(blank=True, null=True, upload_to="static/images"),
        ),
    ]

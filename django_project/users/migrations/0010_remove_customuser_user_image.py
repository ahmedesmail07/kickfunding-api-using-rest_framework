# Generated by Django 4.2 on 2023-05-13 22:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_alter_customuser_user_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="user_image",
        ),
    ]

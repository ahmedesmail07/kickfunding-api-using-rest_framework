# Generated by Django 4.2 on 2023-05-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_customuser_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]

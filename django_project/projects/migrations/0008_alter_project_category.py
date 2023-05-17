# Generated by Django 4.2 on 2023-05-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0007_alter_project_end_date_alter_project_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="category",
            field=models.CharField(
                choices=[
                    ("Health", "Health"),
                    ("Education", "Education"),
                    ("Environment", "Environment"),
                    ("Animal", "Animal"),
                    ("Culture & Art", "Culture & Art"),
                    ("Other", "Other"),
                ],
                default="other",
                max_length=50,
            ),
        ),
    ]
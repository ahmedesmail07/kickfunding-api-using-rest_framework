# Generated by Django 4.2 on 2023-05-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0006_remove_payment_current_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="current_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
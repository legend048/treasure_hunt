# Generated by Django 4.1.7 on 2024-03-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("setup", "0004_alter_event_event_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qr",
            name="image",
            field=models.ImageField(blank=True, upload_to="qr"),
        ),
    ]
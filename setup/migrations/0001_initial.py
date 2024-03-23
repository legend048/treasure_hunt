# Generated by Django 5.0.2 on 2024-03-23 13:08

import django.db.models.deletion
import django.utils.timezone
import setup.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('number_of_qr', models.IntegerField()),
                ('event_active', models.BooleanField(blank=True)),
                ('event_code', models.CharField(default=setup.models.event.generate_unique_value, max_length=12, unique=True)),
                ('event_organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.event')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='qr',
            fields=[
                ('image', models.ImageField(blank=True, upload_to='qr')),
                ('qr_id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('hint', models.CharField(blank=True, max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.event')),
            ],
        ),
        migrations.CreateModel(
            name='scanned_qr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scanned_at', models.DateTimeField(blank=True, null=True)),
                ('qr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.qr')),
                ('scanned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

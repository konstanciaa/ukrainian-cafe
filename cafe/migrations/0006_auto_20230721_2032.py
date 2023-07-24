# Generated by Django 3.2.20 on 2023-07-21 20:32

import cafe.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafe', '0005_auto_20230721_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, null=True, validators=[cafe.models.Booking.validate_date]),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('user', 'first_name', 'last_name', 'booking_date', 'time')},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date_time',
        ),
    ]
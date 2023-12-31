# Generated by Django 3.2.20 on 2023-07-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.IntegerField(choices=[(0, 'Awaiting Confirmation'), (1, 'Booking Confirmed'), (2, 'Booking Declined')], default=0),
        ),
    ]

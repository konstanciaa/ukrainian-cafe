# Generated by Django 3.2.20 on 2023-09-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleganza', '0002_rename_author_booking_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(0, 'Confirmed'), (1, 'Cancelled')], default=0),
        ),
    ]
# Generated by Django 3.2.18 on 2023-04-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleganza', '0005_rename_customer_appointment_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='first_name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

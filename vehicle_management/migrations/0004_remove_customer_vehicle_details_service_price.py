# Generated by Django 3.2.7 on 2021-11-19 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_management', '0003_alter_customer_vehicle_details_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_vehicle_details',
            name='service_price',
        ),
    ]

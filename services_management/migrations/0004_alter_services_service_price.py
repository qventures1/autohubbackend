# Generated by Django 3.2.7 on 2021-11-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_management', '0003_alter_services_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

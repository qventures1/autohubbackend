# Generated by Django 3.2.7 on 2022-01-20 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service_provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service_provider.serviceprovider')),
            ],
        ),
    ]

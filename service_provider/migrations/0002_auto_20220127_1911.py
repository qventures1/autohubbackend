# Generated by Django 3.2.7 on 2022-01-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='latitude',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='longitude',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

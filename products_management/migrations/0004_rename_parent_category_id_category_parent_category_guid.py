# Generated by Django 3.2.7 on 2021-12-03 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_management', '0003_auto_20211203_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent_category_id',
            new_name='parent_category_guid',
        ),
    ]
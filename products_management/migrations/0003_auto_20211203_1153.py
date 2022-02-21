# Generated by Django 3.2.7 on 2021-12-03 06:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products_management', '0002_auto_20211202_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('parent_category_id', models.UUIDField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='products_management.category'),
            preserve_default=False,
        ),
    ]
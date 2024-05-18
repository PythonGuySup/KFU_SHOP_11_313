# Generated by Django 5.0.1 on 2024-05-01 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='cross_store.category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]

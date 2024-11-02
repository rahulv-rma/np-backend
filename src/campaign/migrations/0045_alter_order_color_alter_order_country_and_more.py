# Generated by Django 5.0.6 on 2024-09-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('campaign', '0044_order_color_order_country_order_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='color',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
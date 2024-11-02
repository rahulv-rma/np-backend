# Generated by Django 5.0.6 on 2024-09-02 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('logistics', '0011_employeeorderproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsCenterStockSnapshot',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'center',
                    models.CharField(choices=[('ORIAN', 'Orian')], max_length=100),
                ),
                ('snapshot_date_time', models.DateTimeField()),
                ('snapshot_file_path', models.TextField()),
                ('processed_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LogisticsCenterStockSnapshotLine',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('sku', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                (
                    'stock_snapshot',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='lines',
                        to='logistics.logisticscenterstocksnapshot',
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-26 20:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('campaign', '0040_order_logistics_center_status'),
        ('logistics', '0010_logisticscentermessage_message_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeOrderProduct',
            fields=[],
            options={
                'verbose_name': 'Order Summary',
                'verbose_name_plural': 'Order Summaries',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('campaign.orderproduct',),
        ),
    ]
# Generated by Django 4.2.11 on 2024-04-12 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_total_preparation_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_preparation_time',
        ),
    ]
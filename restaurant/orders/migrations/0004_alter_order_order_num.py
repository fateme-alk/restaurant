# Generated by Django 4.2.11 on 2024-04-12 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_items_alter_order_discount_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_num',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]

# Generated by Django 4.2.11 on 2024-04-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_order_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]

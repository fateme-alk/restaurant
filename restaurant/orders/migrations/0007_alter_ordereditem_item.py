# Generated by Django 4.2.11 on 2024-04-12 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_category_name'),
        ('orders', '0006_alter_order_order_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
    ]

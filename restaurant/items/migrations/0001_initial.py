# Generated by Django 4.2.11 on 2024-04-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('starter', 'starter'), ('main_dish', 'main_dish'), ('dessert', 'dessert')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ingredients', models.TextField()),
                ('preparation_time', models.IntegerField()),
                ('category', models.ManyToManyField(to='items.category')),
            ],
        ),
    ]

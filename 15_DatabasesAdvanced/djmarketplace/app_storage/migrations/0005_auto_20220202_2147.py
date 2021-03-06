# Generated by Django 3.2.5 on 2022-02-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_storage', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='good',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
    ]

# Generated by Django 3.2.5 on 2022-02-01 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_storage', '0002_good_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default='6d35c09f-6453-4904-a6b1-7a125b1d44db', on_delete=django.db.models.deletion.CASCADE, to='app_storage.orderstatus'),
        ),
    ]
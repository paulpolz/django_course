# Generated by Django 3.2.5 on 2022-01-29 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_loyalty', '0002_alter_balance_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='status',
            field=models.ForeignKey(default='Guest', on_delete=django.db.models.deletion.CASCADE, to='app_loyalty.balancestatus'),
        ),
    ]

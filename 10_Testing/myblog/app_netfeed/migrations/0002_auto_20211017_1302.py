# Generated by Django 3.2.5 on 2021-10-17 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_netfeed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeds',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='feed',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_netfeed.feeds'),
        ),
    ]
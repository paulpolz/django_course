# Generated by Django 3.2.5 on 2021-07-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0007_alter_advertisements_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisementauthor',
            name='phone',
            field=models.CharField(default=None, max_length=100),
        ),
    ]

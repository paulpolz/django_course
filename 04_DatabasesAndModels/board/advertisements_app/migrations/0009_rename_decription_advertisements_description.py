# Generated by Django 3.2.5 on 2021-07-25 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0008_advertisementauthor_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisements',
            old_name='decription',
            new_name='description',
        ),
    ]

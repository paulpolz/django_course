# Generated by Django 3.2.5 on 2021-07-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0010_alter_advertisementauthor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementstatus',
            name='name',
            field=models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано'), ('Архив', 'Архив'), ('DL', 'Удалено')], max_length=100),
        ),
    ]

# Generated by Django 3.2.5 on 2022-02-05 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_storage', '0007_auto_20220205_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='store',
            field=models.ManyToManyField(to='app_storage.Store', verbose_name='Store Name'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='store',
        ),
        migrations.AddField(
            model_name='article',
            name='store',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app_storage.store', verbose_name='Store name'),
            preserve_default=False,
        ),
    ]

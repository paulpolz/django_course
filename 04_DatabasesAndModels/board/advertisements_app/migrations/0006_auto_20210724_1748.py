# Generated by Django 3.2.5 on 2021-07-24 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0005_auto_20210724_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementcategory',
            name='name',
            field=models.CharField(choices=[('Авто', 'Авто'), ('Недвижимость', 'Недвижимость'), ('Работа', 'Работа')], max_length=100),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements_app.advertisementcategory', verbose_name='Категория объявления'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements_app.advertisementstatus', verbose_name='Статус объявления'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements_app.advertisementtype', verbose_name='Тип объявления'),
        ),
        migrations.AlterField(
            model_name='advertisementstatus',
            name='name',
            field=models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано'), ('Архив', 'Архив')], max_length=100),
        ),
        migrations.AlterField(
            model_name='advertisementtype',
            name='name',
            field=models.CharField(choices=[('Продам', 'Продам'), ('Куплю', 'Куплю'), ('Сдам', 'Сдам')], max_length=100),
        ),
        migrations.AlterModelTable(
            name='advertisements',
            table='advertisement',
        ),
    ]

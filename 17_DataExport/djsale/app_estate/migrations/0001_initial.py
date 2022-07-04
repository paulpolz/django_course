# Generated by Django 3.2.5 on 2022-02-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyParameter',
            fields=[
                ('parameter_id', models.UUIDField(primary_key=True, serialize=False)),
                ('parameter_name', models.CharField(max_length=50, verbose_name='Parameter name')),
                ('parameter_value', models.CharField(max_length=50, verbose_name='Parameter value')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Property Parameter',
                'verbose_name_plural': 'Property Parameters',
            },
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('property_type_id', models.UUIDField(primary_key=True, serialize=False)),
                ('property_type_lv1', models.CharField(max_length=50, verbose_name='Type of property level 1')),
                ('property_type_lv2', models.CharField(max_length=50, verbose_name='Type of property level 2')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Property Type',
                'verbose_name_plural': 'Property Types',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Property name')),
                ('description', models.TextField(verbose_name='Property description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('is_published', models.BooleanField(verbose_name='Is published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parameter', models.ManyToManyField(to='app_estate.PropertyParameter')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_estate.propertytype')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
    ]

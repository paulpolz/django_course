# Generated by Django 3.2.5 on 2021-09-15 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': (('can_publish', 'can_publish'),), 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
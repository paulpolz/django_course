# Generated by Django 3.2.5 on 2021-09-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_alter_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Ник неавторизованного комментатора'),
        ),
    ]

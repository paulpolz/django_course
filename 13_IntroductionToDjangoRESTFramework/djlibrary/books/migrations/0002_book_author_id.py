# Generated by Django 3.2.5 on 2022-01-06 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.author', verbose_name='Author'),
        ),
    ]

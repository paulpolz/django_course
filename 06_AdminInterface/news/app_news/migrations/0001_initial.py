# Generated by Django 3.2.5 on 2021-08-12 04:24

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('logo', models.ImageField(blank=True, upload_to='images/cates_logo/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nick', models.CharField(max_length=25, verbose_name='Псевдоним пользователя')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия пользователя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
                ('is_author', models.BooleanField(verbose_name='Может ли пользователь публиковать новости?')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок новости')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(verbose_name='Флаг активности')),
                ('views_count', models.BigIntegerField(default=0)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_news.user', verbose_name='Автор')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_news.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('arc', 'Archive'), ('pub', 'Published'), ('del', 'Deleted')], default='arc', max_length=50, verbose_name='Статус комментария')),
                ('comment', models.TextField(max_length=280, verbose_name='Текст комментария')),
                ('news_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_news.news')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_news.user', verbose_name='Имя пользователя')),
            ],
        ),
    ]

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Advertisements(models.Model):
    # TODO перебор для заголовка резервировать строку в 1500 символов. Обычно "строка" для базе данных это до 255
    #  символов. Если нужен такой большой заголовок, то выбирайте тогда поле TextField
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True, db_index=True)
    updated_at = models.DateField(auto_now=True)
    price = models.FloatField(default=0, verbose_name='Цена')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements', verbose_name='Статус объявления')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements', verbose_name='Тип объявления')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements', verbose_name='Владелец объявления')
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements', verbose_name='Категория объявления')

    def __str__(self):
        return self.title


class AdvertisementStatus(models.Model):
    DRAFT = 'Черновик'  # TODO чтобы не заполнять базу "большими строками", обычно тут указывают некий сокращённый вид
    PUBLISHED = 'Опубликовано'
    ARCHIVE = 'Архив'
    DELETED = 'DL'
    AVAILABLE_STATUSES = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
        (ARCHIVE, 'Архив'),
        (DELETED, 'Удалено')
    )
    name = models.CharField(max_length=100, choices=AVAILABLE_STATUSES)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    SALE = 'Продам'
    BUY = 'Куплю'
    RENT = 'Сдам'
    AVAILABLE_TYPES = (
        (SALE, 'Продам'),
        (BUY, 'Куплю'),
        (RENT, 'Сдам')
    )
    name = models.CharField(max_length=100, choices=AVAILABLE_TYPES)
    
    def __str__(self):
        return self.name


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    # phone = models.CharField(max_length=100, default=None)
    phone = PhoneNumberField()
    
    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    AUTO = 'Авто'
    PROPERTY = 'Недвижимость'
    JOB = 'Работа'
    AVAILABLE_CATES = (
        (AUTO,	'Авто'),
        (PROPERTY,	'Недвижимость'),
        (JOB,	'Работа')
    )
    name = models.CharField(max_length=100, choices=AVAILABLE_CATES)

    def __str__(self):
        return self.name

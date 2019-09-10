from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    department_choices = (
        ('Смартфон', 'Смартфон'),
        ('Автомобиль', 'Автомобиль'),
        ('Мебель', 'Мебель'),
        ('Велосипед', 'Велосипед'),
        ('Без категории', 'Без категории')
    )
    item_name = models.CharField(max_length=40, verbose_name='Наименование')
    department = models.CharField(max_length=15, choices=department_choices, default='Без категории', verbose_name='Категория')
    text = models.TextField(max_length=200, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    email = models.EmailField()
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')

    '''def publish(self):
        self.published_date = timezone.now()
        self.save()
    '''
    def __str__(self):
        return self.item_name

class User_r(models.Model):
    username = models.CharField(max_length=18, verbose_name='Логин')
    name = models.CharField(max_length=15, verbose_name='Имя')
    email = models.EmailField()
    password = models.CharField(max_length=64, verbose_name='Пароль')

    def __str__(self):
        return self.username

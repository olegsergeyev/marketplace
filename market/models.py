from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Item(models.Model):
    department_choices = (
        ('Smartphone', 'Смартфон'),
        ('Car', 'Автомобиль'),
        ('Furniture', 'Мебель'),
        ('Bike', 'Велосипед'),
        ('NoCat', 'Без категории')
    )
    item_name = models.CharField(max_length=40)
    department = models.CharField(max_length=15, choices=department_choices, default='NoCat')
    text = models.TextField()
    price = models.IntegerField()
    email = models.EmailField(default='sanek@gmail.com')
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

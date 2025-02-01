from django.db import models
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique = True, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('smartphone','Смартфон'),
        ('headphones','Наушники'),
        ('watch','Часы'),
    ]

    name = models.CharField(max_length = 100, verbose_name = 'Название товара')
    category = models.CharField(max_length = 20, choices = CATEGORY_CHOICES, verbose_name = 'Категория')
    description = models.TextField(verbose_name = 'Описание товара')
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Цена')
    stock = models.PositiveIntegerField(verbose_name = 'Количество на складе')
    image = models.ImageField(upload_to = 'products/', verbose_name = 'Изображение товара', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата добавления')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Дата обновления')

    def clean(self):
        """Проверка валидности данных перед сохранением"""
        if self.price < 0:
            raise ValidationError({'price': 'Цена не может быть отрицательной.'})

    def __str__(self):
        return self.name   



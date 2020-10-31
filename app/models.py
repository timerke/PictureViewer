from django.db import models


class Picture(models.Model):
    title = models.CharField(max_length=30)  # название картинки
    description = models.CharField(max_length=300)  # описание картинки
    date = models.DateField(auto_now=True)  # дата сохранения
    filename = models.CharField(max_length=100)  # путь к картинке на сервере

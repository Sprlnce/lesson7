from django.db import models
from django.contrib import admin
from django.utils import timezone, html

# Create your models here.

class Advertisement(models.Model): # это класс-модель
    # он реализует таблицу Advertisment
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("описание")
    author = models.CharField("автор", max_length=64)
    price = models.FloatField("цена")
    auction = models.BooleanField("торг", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "advertisements"
       
    def __str__(self) -> str:
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"
    

# from app_advertisment.models import Advertisement
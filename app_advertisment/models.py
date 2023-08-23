from django.db import models
from django.contrib import admin
from django.utils import timezone, html
from django.utils import timezone
from django.utils.html import format_html


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

    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green; font-weight: bold;">Сегодня в {}</span>', create_time
            )
        return self.created_at.strftime('%d.%m.%y at %H:%M:%S')
        

    @admin.display(description="Дата обновления")
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:purple; font-weight: bold;">Сегодня в {}</span>', update_time
            )
        return self.update_at.strftime('%d.%m.%y at %H:%M:%S')
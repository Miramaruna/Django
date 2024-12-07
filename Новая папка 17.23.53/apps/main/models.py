from django.db import models
from apps.utils import custom_upload_path

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок сайта"
    )
    desciption = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to=custom_upload_path
    )
    instagram = models.URLField(
        verbose_name='Ссылка на Instagram',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Ссылка на Facebook'
    )
    youtube = models.URLField(
        verbose_name='Ссылка на Youtube'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'ОСновные настройки'
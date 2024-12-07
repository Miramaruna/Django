from django.db import models
from apps.utils import custom_upload_path

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to=custom_upload_path
    )
    instagram = models.URLField(
        verbose_name='Ссылка на instagram',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Ссылка на youtube',
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Основная настройка"
        verbose_name_plural = "Основные настроки"
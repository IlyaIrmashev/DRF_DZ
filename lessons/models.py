from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='lessons/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    video = models.TextField(**NULLABLE, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

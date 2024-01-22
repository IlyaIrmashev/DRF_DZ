from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    the_user = 'visitor', gettext_lazy('visitor')
    moderator = 'moderator', gettext_lazy('moderator')


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=150, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    role = models.CharField(max_length=20, **NULLABLE, choices=UserRoles.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

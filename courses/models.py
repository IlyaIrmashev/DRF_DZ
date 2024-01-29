from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='courses/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Покупатель курса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='lessons/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    video = models.TextField(**NULLABLE, verbose_name='Ссылка')
    course_lesson = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='Урок курса')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Покупатель урока')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('Cash', 'Наличные'),
        ('Transfer', 'Перевод')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_payment = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченый курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченый урок')
    payment_amount = models.PositiveIntegerField('Сумма оплаты')
    payment_method = models.CharField(max_length=150, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')

    is_paid = models.BooleanField(default=False, verbose_name='оплачено')
    payment_intent_id = models.CharField(default='NULL', max_length=100, verbose_name='id_платежа')

    def __str__(self):
        return f'{self.user}: {self.paid_course if self.paid_course else self.paid_lesson} - {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status_subscription = models.BooleanField(default=True, verbose_name='Статус подписки')

    def __str__(self):
        return f'{self.user} : {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'



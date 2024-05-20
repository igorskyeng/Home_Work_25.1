from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)

    USERNAME_FIELD = "email"
    username = USERNAME_FIELD
    REQUIRED_FIELDS = []


class Payments(models.Model):

    class PaymentMethod(models.TextChoices):
        CASH = "Наличные", "Наличные"
        TRANSFER = "Перевод", "Перевод"

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользватель', null=True)
    payment_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, verbose_name='Название курса', on_delete=models.CASCADE)
    payment_amount = models.IntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=50, default=PaymentMethod.CASH,
                                      choices=PaymentMethod, verbose_name='Метод оплаты')

    def __str__(self):
        return str(self.paid_course)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('id',)

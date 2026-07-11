from django.db import models
from django.utils import timezone

from users.models import User


class Specialization(models.Model):
    """Модель специализация"""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="название специализация",
        help_text="Укажите специализацию",
    )
    preview = models.ImageField(
        null=True,
        blank=True,
        verbose_name="Изображение специализации",
        help_text="Загрузите изображение специализации",
    )
    description = models.TextField(
        verbose_name="Описание специализации",
        help_text="Введите описание специализации",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Service(models.Model):
    """Модель услуга"""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название услуга",
        help_text="Укажите название услуги",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание услуги",
        help_text="Укажите описание услуги",
    )
    preview = models.ImageField(null=True, blank=True)
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        verbose_name="Специализация",
        help_text="Укажите специализацию",
    )
    price = models.IntegerField(
        verbose_name="Стоимость услуги", default=0, help_text="Укажите стоимость услуги"
    )
    working_day = models.IntegerField(blank=True, null=True)
    working_month = models.IntegerField(blank=True, null=True)
    working_hour = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Appointment(models.Model):
    """Модель записи на прием"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор записи",
        null=True,
        blank=True,
    )
    name = models.CharField(default="Иван", max_length=100)
    last_name = models.CharField(default="Иванов", max_length=100)

    phone = models.CharField(default=70000000, max_length=100)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name="Услуга"
    )
    created_at = models.DateTimeField(
        verbose_name="Создание записи", default=timezone.now
    )
    updated_at = models.DateTimeField(
        verbose_name="Изменение записи", default=timezone.now
    )

    order_day = models.DateField(null=True, blank=True)
    order_time = models.TimeField(null=True, blank=True)


class Employee(models.Model):
    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Медицинский работник",
    )
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, verbose_name="Специализация"
    )

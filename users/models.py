from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель Юзер"""

    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True)
    token = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="token"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

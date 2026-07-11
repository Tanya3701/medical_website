from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Представление страницы администратора для класса Пользователь"""

    list_display = ("id", "email")

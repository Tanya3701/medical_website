from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """Стандартная форма класса Пользователь"""

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

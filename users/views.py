import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView

from config import settings
from medical_website.models import Appointment
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    """Класс создания экземпляра класса Пользователь"""

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Получение токена текущем пользователем"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Верификация",
            message=f"Здравствуйте, перейдите по ссылке для подтверждения {url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Верификация пользователя по токену"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class PersonalAccountView(TemplateView):
    """Класс представления страницы личного кабинета пользователя"""

    model = User
    form_class = UserRegisterForm
    template_name = "users/personal_account.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        """Получение контекстных данных из родительского класса"""
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        appointments = Appointment.objects.filter(owner=user)
        context["appointments"] = appointments

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.views import email_verification, UserCreateView, PersonalAccountView

app_name = UsersConfig.name


urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("email-confirm/<str:token>/", email_verification, name="email_confirm"),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="password_reset_form.html",
            email_template_name="password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
        name="password_reset_complete",
    ),
    path("personal_account/", PersonalAccountView.as_view(), name="personal_account"),
]

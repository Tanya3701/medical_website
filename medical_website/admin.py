from django.contrib import admin

from medical_website.models import Specialization, Service, Appointment


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Представление страницы администратора для класса Категории"""
    list_display = ("name", "description")
    fields = ("name", "description")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Представление страницы администратора для класса Услуги"""
    list_display = ("name", "description")
    fields = ("name", "description", "specialization")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Представление страницы администратора для класса Запись"""
    list_display = ("name", "last_name", "phone", "service", "order_day", "order_time")
    fields = ("name", "last_name", "phone", "service", "order_day", "order_time")

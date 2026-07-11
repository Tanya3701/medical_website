from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from rest_framework.reverse import reverse_lazy

from medical_website.forms import (AppointmentForm, ServiceForm,
                                   SpecializationForm)
from medical_website.models import Appointment, Service, Specialization
from medical_website.services import ServicesService

ALL_TIME = [
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
]


class MedicalWebsiteView(TemplateView):
    """Класс представления главной страницы"""

    template_name = "medical_website/main.html"

    def get_context_data(self, **kwargs):
        """Получение контекстных данных из родительского класса"""
        context = super().get_context_data(**kwargs)
        specializations = Specialization.objects.all()
        context["specializations"] = specializations


class SpecializationListView(ListView):
    """Класс представления списка категорий"""

    model = Specialization
    context_object_name = "specializations"


class SpecializationDetailView(DetailView):
    """Класс представления одной категорий"""

    model = Specialization
    context_object_name = "specialization"


class SpecializationCreateView(CreateView):
    """Класс представления создания категорий"""

    model = Specialization
    context_object_name = "specialization"
    success_url = reverse_lazy("medical_website:specialization_list")
    form_class = SpecializationForm


class SpecializationUpdateView(UpdateView):
    """Класс представления редактирования категорий"""

    model = Specialization
    context_object_name = "specialization"
    success_url = reverse_lazy("medical_website:specialization_list")
    form_class = SpecializationForm


class SpecializationDeleteView(DeleteView):
    """Класс представления удаления категорий"""

    model = Specialization
    context_object_name = "specialization"
    success_url = reverse_lazy("medical_website:specialization_list")


class ServiceDetailView(DetailView):
    """Класс представления одной услуги"""

    model = Service
    context_object_name = "service"


class ServiceCreateView(CreateView):
    """Класс представления создания услуги"""

    model = Service
    context_object_name = "service"
    success_url = reverse_lazy("medical_website:specialization_list")
    form_class = ServiceForm


class ServiceUpdateView(UpdateView):
    """Класс представления редактирования услуги"""

    model = Service
    context_object_name = "service"
    success_url = reverse_lazy("medical_website:specialization_list")
    form_class = ServiceForm


class ServiceDeleteView(DeleteView):
    """Класс представления удаления услуги"""

    model = Service
    context_object_name = "service"
    success_url = reverse_lazy("medical_website:specialization_list")


class AboutUsView(TemplateView):
    """Класс представления страницы о нас"""

    template_name = "medical_website/about_us.html"


class ContactsView(TemplateView):
    """Класс представления страницы контакты"""

    template_name = "medical_website/contacts.html"


class ServiceBySpecializationView(ListView):
    """Класс представления услуг по категориям"""

    def get_queryset(self):
        specialization_id = self.kwargs.get("specialization_id")
        return ServicesService.get_service_by_id(specialization_id)

    def get_context_data(self, **kwargs):
        """Получение контекстных данных из родительского класса"""
        context = super().get_context_data(**kwargs)
        specialization_id = self.kwargs.get("specialization_id")
        context["service_by_specialization"] = ServicesService.get_service_by_id(
            specialization_id=specialization_id
        )
        return context


class AppointmentCreateView(CreateView, LoginRequiredMixin):
    """Класс представления создания записи"""

    model = Appointment
    context_object_name = "appointment"
    success_url = reverse_lazy("medical_website:success_appointment")
    form_class = AppointmentForm

    def form_valid(self, form):
        """Присвоение авторства записи текущему пользователю"""
        appointment = form.save()
        user = self.request.user
        appointment.owner = user
        appointment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Получение контекстных данных из родительского класса"""
        context = super().get_context_data(**kwargs)
        all_time = ALL_TIME
        context["all_time"] = all_time

        today_date = datetime.today()
        max_date = today_date + timedelta(days=30)
        today = today_date.strftime("%Y-%m-%d")
        max_day = max_date.strftime("%Y-%m-%d")
        context["today"] = today
        context["max_day"] = max_day
        return context

    def post(self, request, *args, **kwargs):
        """Получение данных пользователя для создания экземпляра класса"""
        if request.method == "POST":
            form = AppointmentForm(request.POST)
            if form.is_valid():
                appointment = form.save()
                user = self.request.user
                appointment.owner = user
                service_id = request.POST.get("service")
                service = Service.objects.get(id=service_id)
                name = request.POST.get("name")
                last_name = request.POST.get("last_name")
                phone = request.POST.get("phone")
                order_day = request.POST.get("date")
                order_time = request.POST.get("time")
                appointment = Appointment(
                    name=name,
                    last_name=last_name,
                    phone=phone,
                    order_day=order_day,
                    order_time=order_time,
                    service=service,
                )
                appointment.save()
                return render(
                    request,
                    "medical_website/success_appointment.html",
                    {
                        "appointment": appointment,
                        "name": name,
                        "last_name": last_name,
                        "phone": phone,
                        "order_day": order_day,
                        "order_time": order_time,
                        "service": service.name,
                    },
                )
            else:
                return render(request, "medical_website/form.html", {"form": form})


class SuccessAppointmentView(DetailView):
    """Класс представления страницы удачной записи"""

    model = Appointment
    context_object_name = "appointment"
    template_name = "medical_website/success_appointment.html"

    def get_context_data(self, **kwargs):
        """Получение контекстных данных из родительского класса"""
        context = super().get_context_data(**kwargs)
        appointment = self.object
        context["appointment"] = appointment

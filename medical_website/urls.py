from django.urls import path

from medical_website.apps import MedicalWebsiteConfig
from medical_website.views import (AboutUsView, AppointmentCreateView,
                                   ContactsView, MedicalWebsiteView,
                                   ServiceBySpecializationView,
                                   ServiceCreateView, ServiceDeleteView,
                                   ServiceDetailView, ServiceUpdateView,
                                   SpecializationCreateView,
                                   SpecializationDeleteView,
                                   SpecializationDetailView,
                                   SpecializationListView,
                                   SpecializationUpdateView,
                                   SuccessAppointmentView)

app_name = MedicalWebsiteConfig.name


urlpatterns = [
    path("main/", MedicalWebsiteView.as_view(), name="main"),
    path(
        "specialization/list/",
        SpecializationListView.as_view(),
        name="specialization_list",
    ),
    path(
        "specialization/create/",
        SpecializationCreateView.as_view(),
        name="specialization_create",
    ),
    path(
        "specialization/detail/<int:pk>/",
        SpecializationDetailView.as_view(),
        name="specialization_detail",
    ),
    path(
        "specialization/<int:pk>/update/",
        SpecializationUpdateView.as_view(),
        name="specialization_update",
    ),
    path(
        "specialisation/<int:pk>/delete/",
        SpecializationDeleteView.as_view(),
        name="specialization_delete",
    ),
    path(
        "service/list/<int:specialization_id>",
        ServiceBySpecializationView.as_view(),
        name="service_list",
    ),
    path("service/create/", ServiceCreateView.as_view(), name="service_create"),
    path(
        "service/detail/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"
    ),
    path(
        "service/<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"
    ),
    path(
        "service/<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_delete"
    ),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path(
        "appointment/create/",
        AppointmentCreateView.as_view(),
        name="appointment_create",
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "success_appointment/",
        SuccessAppointmentView.as_view(),
        name="success_appointment",
    ),
]

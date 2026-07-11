from django.urls import path

from medical_website.apps import MedicalWebsiteConfig
from medical_website.views import (
    MedicalWebsiteView,
    SpecializationDetailView,
    SpecializationListView,
    SpecializationCreateView,
    SpecializationUpdateView,
    SpecializationDeleteView,
    ServiceCreateView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceDeleteView,
    AboutUsView,
    AppointmentDeleteView,
    AppointmentListView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDetailView,
    ContactsView,
    ServiceBySpecializationView,
    SuccessAppointmentView,
)

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
    path("appointment/list/", AppointmentListView.as_view(), name="appointment_list"),
    path(
        "appointment/create/",
        AppointmentCreateView.as_view(),
        name="appointment_create",
    ),
    path(
        "appointment/<int:pk>/update/",
        AppointmentUpdateView.as_view(),
        name="appointment_update",
    ),
    path(
        "appointment/<int:pk>/delete/",
        AppointmentDeleteView.as_view(),
        name="appointment_delete",
    ),
    path(
        "appointment/detail/<int:pk>/",
        AppointmentDetailView.as_view(),
        name="appointment_detail",
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "success_appointment/",
        SuccessAppointmentView.as_view(),
        name="success_appointment",
    ),
]

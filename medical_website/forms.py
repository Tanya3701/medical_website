from django.forms import ModelForm

from medical_website.models import Specialization, Service, Appointment


class SpecializationForm(ModelForm):
    class Meta:
        model = Specialization
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SpecializationForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование категории"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание категории"}
        )


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование сервиса"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание сервиса"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Задайте стоимость сервиса"}
        )


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ["name", "last_name", "phone", "service"]

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите имя"}
        )
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите фамилию"}
        )

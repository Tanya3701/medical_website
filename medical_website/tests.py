from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from medical_website.models import Specialization, Service


class SpecializationTest(TestCase):
    """Тестирование представлений класса категории"""
    def setUp(self):
        self.specialization = Specialization.objects.create(
            name="Test", description="Test"
        )

    def test_specialization_detail(self):
        """Тест представления одного экземпляра класса"""
        url = reverse(
            "medical_website:specialization_detail", args=(self.specialization.pk,)
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_specialization_create(self):
        """Тест представления создания экземпляра"""
        url = reverse("medical_website:specialization_create")
        data = {"name": "Test2", "description": "Test2"}
        self.client.post(url, data)
        self.assertEqual(Specialization.objects.count(), 2)

    def test_specialization_update(self):
        """Тест представления редактирования экземпляра"""
        url = reverse(
            "medical_website:specialization_update", args=(self.specialization.pk,)
        )
        data = {"name": "Test3", "description": "Test3"}
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Test3")

    def test_specialization_delete(self):
        """Тест представления удаления экземпляра"""
        url = reverse(
            "medical_website:specialization_delete", args=(self.specialization.pk,)
        )
        self.client.delete(url)
        self.assertEqual(Specialization.objects.count(), 0)

    def test_specialization_list(self):
        """Тест представления списка экземпляров класса"""
        url = reverse("medical_website:specialization_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ServiceTest(TestCase):
    """Тест представления класса услуг"""
    def setUp(self):
        self.specialization = Specialization.objects.create(
            name="Test", description="Test"
        )
        self.service = Service.objects.create(
            name="Test",
            description="Test",
            price=100,
            specialization=self.specialization,
        )

    def test_service_detail(self):
        """Тест представления одного экземпляра класса"""
        url = reverse("medical_website:service_detail", args=(self.service.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_service_create(self):
        """Тест представления создания экземпляра"""
        url = reverse("medical_website:service_create")
        data = {
            "name": "Test2",
            "description": "Test2",
            "price": 150,
            "specialization": self.specialization.pk,
        }
        self.client.post(url, data)
        self.assertEqual(Service.objects.count(), 2)

    def test_service_update(self):
        """Тест представления редактирования экземпляра"""
        url = reverse("medical_website:service_update", args=(self.service.pk,))
        data = {
            "name": "Test3",
            "description": "Test3",
            "price": 150,
            "specialization": self.specialization.pk,
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Test3")

    def test_service_delete(self):
        """Тест представления удаления экземпляра"""
        url = reverse("medical_website:service_delete", args=(self.service.pk,))
        self.client.delete(url)
        self.assertEqual(Specialization.objects.count(), 1)

    def test_service_list(self):
        """Тест представления списка экземпляров класса"""
        url = reverse("medical_website:service_list", args=(self.specialization.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

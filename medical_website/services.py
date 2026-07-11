from medical_website.models import Service


class ServicesService(Service):
    @staticmethod
    def get_service_by_id(specialization_id):
        """Сортирует услуги по категориям"""
        services = Service.objects.filter(specialization_id=specialization_id)
        if services is not None:
            return services
        return None

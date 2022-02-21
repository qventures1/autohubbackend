"""
All view related to the service provider

"""

from service_provider.service_provider_controller import ServiceProviderController
from rest_framework.views import APIView


class ServiceProvierView(APIView):
    """CRUD Api view for the service provider"""

    sp_controller = ServiceProviderController()

    def post(self, request):
        """Create a Service Provider"""

        return self.sp_controller.create_service_provider(request)

    def get(self, request):
        """Get details of a Service Provider"""

        return self.sp_controller.get_service_provider(request)





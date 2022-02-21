from django.shortcuts import render
from rest_framework.views import APIView
from services_management.services_management_controller import ServiceController,ServiceProviderServicesController
# Create your views here.

class ServiceView(APIView):

    service_controller=ServiceController()

    def post(self,request):
        """create service """

        return self.service_controller.create_services(request)

    def get(self,request):
        """show service"""

        return self.service_controller.Show_services(request)

    def patch(self,request):
        """update service by id"""

        return self.service_controller.update_services(request)

    def delete(self,request):
        """delete sevice by id"""

        return self.service_controller.delete_service(request)


class ServiceProviderServicesView(APIView):
    ServiceProviderServices_controller=ServiceProviderServicesController()
    def post(self,request):
        """add service provider service"""

        return self.ServiceProviderServices_controller.add_service_provider_services(request)

    def  get(self,request):

        return self.ServiceProviderServices_controller.Show_service_provider_services(request)


    def patch(self,request):

        return self.ServiceProviderServices_controller.update_service_provider_services(request)

    def delete(self,request):

        return self.ServiceProviderServices_controller.delete_service_provider_service(request)
from services_management.models import Service_Provider_Services
from vehicle_management.models import Customer_Vehicle_Details
from services_management.models import Services
from utils.response_utils import create_message,create_response
from services_management.serializers import ServicesWriteSerializer,ServiceProviderServicesWriteSerializer,ServicesReadSerializer,ServiceProviderServicesReadSerializer
from django.db import transaction
from utils.request_utils import get_query_param_or_default
from vehicle_management.serializers import CustomerVehicleDetailsWriteSerializer

class ServiceController:
    """Controller class for the services"""

    def create_services(self,request):
        """Create a service"""

        try:
            payload=request.data.copy()
            mandatory_keys=[
                "service_name",
                "description",
            ]
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys,100),400)

            serialzed=ServicesWriteSerializer(data=payload)
            if serialzed.is_valid():
                service=serialzed.save()
            else:
                return create_response(create_message([serialzed.errors],102),400)

            serialzed=ServicesReadSerializer(service)
            return create_response(create_message([serialzed.data],442),200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)


    def Show_services(self, request):
        """Fetch all services details

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:


            services =Services.objects.all().order_by("created_at")


            if not services:
                return create_response(create_message([], 443), 404)

            serialized = ServicesReadSerializer(services,many=True)

            return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def update_services(self,request):
        """Update service information

        Args:
            request ([WSGI]): [description]

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Get mutable copy of request payload
            payload=request.data.copy()

            # guid is mandatory in form data
            if not payload.get("guid",None):
                return create_response(create_message([], 445),400)

            service=Services.objects.filter(guid=payload.get("guid",None)).first()
            # If guid does not exist
            if not service:
                return create_response(create_message([],443),404)
            # guid cannot be updated
            payload.pop("guid",None)


            serialized = ServicesWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(service, serialized.validated_data)
                    read_serialized = ServicesReadSerializer(service)

            return create_response(create_message(read_serialized.data, 444), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_service(self, request):
        """Delete service by id"""

        try:

            # guid is mandatory in query params
            if not get_query_param_or_default(request, "guid", None):
                return create_response(create_message([], 445), 400)

            service = Services.objects.filter(
                guid=get_query_param_or_default(request, "guid", None)
            ).first()

            # If service does not exist
            if not service:
                return create_response(create_message([], 443), 404)

            service.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


class ServiceProviderServicesController:
    """service provider services controller"""

    def add_service_provider_services(self,request):

        try:
            payload=request.data.copy()
            mandatory_keys=[
                "service_name",
                "service_type",
                "duration",
                "description",
                "relevant_technicians",
                "vehicle_brand",
                "vehicle_Type",
                "service_price"
            ]

            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message([mandatory_keys],100),400)

            serialized=CustomerVehicleDetailsWriteSerializer(data=payload)
            if serialized.is_valid():
                vehicle=serialized.save()
            else:
                return create_response(create_message([serialized.errors],102),400)

            vehicle_id=Customer_Vehicle_Details.objects.get(guid=vehicle.guid)

            service=Service_Provider_Services.objects.create(
                service_name=payload.get("service_name"),
                service_type=payload.get("service_type"),
                duration=payload.get("duration"),
                description=payload.get("description"),
                relevant_technicians=payload.get("relevant_technicians"),
                fixed_price=payload.get("fixed_price"),
                rule_based=payload.get("rule_based"),
                service_on_site=payload.get("service_on_site"),
                vehicle=vehicle_id,
                service_price=payload.get("service_price")
            )
            serialized=ServiceProviderServicesReadSerializer(service)
            return create_response(create_message([serialized.data],446),200)
        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)


    def Show_service_provider_services(self, request):
        """Fetch all services details

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:


            services =Service_Provider_Services.objects.all().order_by("created_at")


            if not services:
                return create_response(create_message([], 443), 404)

            serialized = ServiceProviderServicesReadSerializer(services,many=True)

            return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def update_service_provider_services(self,request):
        """Update services information

        Args:
            request ([WSGI]): [description]

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Get mutable copy of request payload
            payload=request.data.copy()

            # guid is mandatory in form data
            if not payload.get("guid",None):
                return create_response(create_message([], 445),400)

            service=Service_Provider_Services.objects.filter(guid=payload.get("guid",None)).first()
            # If guid does not exist
            if not service:
                return create_response(create_message([],443),404)
            # guid cannot be updated
            payload.pop("guid",None)


            serialized = ServiceProviderServicesWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(service, serialized.validated_data)
                    read_serialized = ServiceProviderServicesReadSerializer(service)

            return create_response(create_message(read_serialized.data, 447), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)




    def delete_service_provider_service(self, request):
        """Delete service by id"""

        try:

            # guid is mandatory in query params
            if not get_query_param_or_default(request, "guid", None):
                return create_response(create_message([], 445), 400)

            service = Service_Provider_Services.objects.filter(
                guid=get_query_param_or_default(request, "guid", None)
            ).first()

            # If service does not exist
            if not service:
                return create_response(create_message([], 443), 404)

            service.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)
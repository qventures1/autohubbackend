"""
Controller for all business logic directly related to Service Provider

"""


from service_provider.models import ServiceProvider
from utils.request_utils import get_query_param_or_default
from service_provider.serializers import ServiceProviderReadSerializer, ServiceProviderWriteSerializer
from utils.response_utils import create_message, create_response


class ServiceProviderController:
    """Controller class for the service provider"""

    def create_service_provider(self, request):
        """Create a service provider"""

        try:

            # Get a mutable copy of request payload
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "name",
                "contact_no",
                "description",
                "latitude",
                "longitude"
            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized = ServiceProviderWriteSerializer(data=payload)

            if serialized.is_valid():

                serialized.save()

            else: # There were errors while serializing the payload
                return create_response(create_message([serialized.errors], 102), 400)


            return create_response(create_message([serialized.data], 301), 201)


        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)




    def get_service_provider(self, request):
        """Get details of a service provider"""


        try:

            # Email is mandatory in query params
            # if not get_query_param_or_default(request, "contact_no", None):
            #     return create_response(create_message([], 105), 400)

            payload=request.data.copy()
            service_provider = ServiceProvider.objects.filter(
                contact_no=payload.get("contact_no")
            ).first()
            # service_provider = ServiceProvider.objects.filter(
            #     contact_no=get_query_param_or_default(request, "contact_no", None)
            # ).first()

            if not service_provider:
                return create_response(create_message([], 302), 404)

            serialized = ServiceProviderReadSerializer(service_provider)

            return create_response(create_message([serialized.data], 1000), 200)


        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)




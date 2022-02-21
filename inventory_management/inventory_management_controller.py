"""
Controller class for Inventory management

"""
from django.db import transaction
from django.http import response
from inventory_management.models import Vendor
from inventory_management.serializers import VendorReadSerializer
from rest_framework.serializers import Serializer
from user_profile.user_controller import UserProfileController
from utils.response_utils import create_message, create_response
from inventory_management.serializers import VendorWriteSerializer
from user_profile.models import User,UserType
from service_provider.models import ServiceProvider
from user_profile.serializers import (UserProfileReadSerializer,
                                      UserProfileWriteSerializer)
from utils.request_utils import get_query_param_or_default
from django.http import request
from django.contrib.auth.hashers import make_password
import uuid

class InventoryManagement:
    """controll class for Inventory management"""

    user_controller = UserProfileController()

    def creat_vendor(self,request):
        """Create an vendor

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:
            # Get mutable copy of request.data
            payload=request.data.copy()

            # Mandatory keys in the request payload
            mandatory_key=[
                "name",
                "contact_number",
                "email",
                "address",
                "user_type",
            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_key):
                return create_response(create_message(mandatory_key,100),400)

              # Check if user type id is in the supported user types model
            if not int(payload.get("user_type")) in list(UserType.objects.all().values_list("id", flat=True)):
                return create_response(create_message([], 101), 400)

           # By default user status will be Active i.e. 1
            payload["user_status"] = 1

           # Create User first using existing api in user controller
            payload["password"]=make_password(payload.get("password"))

            serialized=UserProfileWriteSerializer(data=payload)
            if serialized.is_valid():
                serialized.save()
            # # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            # Get service provider
            sp = ServiceProvider.objects.filter(
                guid=payload.get('service_provider')
            ).first()

            vendor = Vendor.objects.create(

                # user=User.objects.get("guid"))
             user=User.objects.get(contact_number=payload.get("contact_number")),
             service_provider = sp
            #  is_origional_manufacturer=payload.get("is_origional_manufacturer")
             )

            serialized=VendorReadSerializer(vendor)

            return create_response(create_message([serialized.data],434),201)

        except Exception as ex:

            return create_response(create_message([str(ex)],1002),500)



    def show_vendor(self,request):
        """Fetch vendor with the given contact number in query params

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """
        try:
            # Contact number is mandatory in query params
            if not get_query_param_or_default(request,"contact_number",None):
                return create_response(create_message([], 436),400)

            vendor=Vendor.objects.filter(
                user__contact_number=get_query_param_or_default(request,"contact_number",None)
            ).first()

            # if vendor does not exist
            if not vendor:
                return create_response(create_message([],435),404)

            serialized=VendorReadSerializer(vendor)
            return create_response(create_message([serialized.data],1000),200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex),1002]),500)



    def update_vendor(self,request):
        """Update vendor with the given contact number in query params

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """
        try:
            payload=request.data.copy()
            print(payload)

            if not payload.get("contact_number",None):
                return create_response(create_message([],436),400)

            vendor=User.objects.filter(contact_number=payload.get("contact_number",None)).first()
            if not vendor:
                return create_response(create_message([],435),404)

            payload.pop("contact_number",None)

            payload.pop("password",None)

            # pop status if status 0 is passed
            payload.pop("status") if payload.get("status",None) and int(payload.get("status")) ==0 else ""

            serialized=UserProfileWriteSerializer(data=payload, partial=True)
            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(vendor,serialized.validated_data)
            read_serialized=UserProfileReadSerializer(vendor)

            return create_response(create_message([read_serialized.data],437),200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_vendor(self, request):
        """Delete vendor i.e. Change vendor status to delete"""

        try:

            # contact number is mandatory in query params
            if not get_query_param_or_default(request, "contact_number", None):
                return create_response(create_message([], 105), 400)

            vendor = User.objects.filter(
                contact_number=get_query_param_or_default(request, "contact_number", None)
            ).first()

            # If vendor does not exist
            if not vendor:
                return create_response(create_message([], 435), 404)

            # Set vendor status to deleted
            vendor.status_id = 0

            # append deleted and uuid at the end of contact number so the contact number
            # can be used again for vendor creation
            vendor.contact_number = vendor.contact_number + "deleted" + str(uuid.uuid4())

            vendor.save()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)

"""
Controller class for customer management

"""
from django.http import response
from rest_framework.serializers import Serializer
from customer_management.models import CustomerProfile
from user_profile.user_controller import UserProfileController
from utils.response_utils import create_message, create_response
from django.contrib.auth.hashers import make_password
from customer_management.serializers import CustomerProfileReadSerializer
from user_profile.models import User,UserType
from user_profile.serializers import (UserProfileReadSerializer,
                                      UserProfileWriteSerializer)
import pyotp

def generate_hash():
        return pyotp.random_base32()
class CustomerManagement:
    """controll class for customer management"""

    user_controller = UserProfileController()

    def creat_customer_profile(self,request):
        """Create an customer profile

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
                "password",
                "contact_number",
            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_key):
                return create_response(create_message(mandatory_key,100),400)

            # user type
            payload["user_type"]=5

              # Check if user type id is in the supported user types model
            if not int(payload.get("user_type")) in list(UserType.objects.all().values_list("id", flat=True)):
                return create_response(create_message([], 101), 400)

           # By default user status will be Active i.e. 1
            payload["status"] = 1

           # Create User first using existing api in user controller
            payload["password"]=make_password(payload.get("password"))

            payload["mf_hash"]=generate_hash()

            serialized=UserProfileWriteSerializer(data=payload)
            if serialized.is_valid():
                user=serialized.save()
                user.generate_token()
            # # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)

            customer = CustomerProfile.objects.create(

                # user=User.objects.get("guid"))
             user=User.objects.get(contact_number=payload.get("contact_number")))

            serialized=CustomerProfileReadSerializer(customer)

            return create_response(create_message([serialized.data],430),201)

        except Exception as ex:

            return create_response(create_message([str(ex)],1002),500)



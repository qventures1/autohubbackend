"""
Controller class for the User Profile app

All business logic related to user management is contained here

"""


import uuid
from pyotp import otp
from user_profile.models import User, UserType
from user_profile.serializers import (UserProfileReadSerializer,
                                      UserProfileWriteSerializer)
from user_profile.user_helper import UserProfileHelper
from utils.request_utils import get_query_param_or_default
from utils.response_utils import create_message, create_response
from django.db import transaction
from django.contrib.auth.hashers import make_password
import pyotp


def generate_hash():
        return pyotp.random_base32()
class UserProfileController:
    """Controller for the business logic of user profile app"""

    user_helper = UserProfileHelper()



    def create_user(self, request):
        """Create user with the given request payload

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        # Get mutable copy of request.data
        payload = request.data.copy()

        try:
            # Mandatory keys in the request payload
            mandatory_keys = [
                "user_type", # The type of user to be created
                "password",
                "contact_number"
            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)

            # Check if user type id is in the supported user types model
            if not int(payload.get("user_type")) in list(UserType.objects.all().values_list("id", flat=True)):
                return create_response(create_message([], 101), 400)

            # if not ServiceProvider.objects.filter(guid=payload.get("sp_guid")).exists():
            #     return create_response(create_message([], 109), 400)

            # By default user status will be Active i.e. 1
            payload["status"] = 1

            # Hash plain text password
            payload["password"] = make_password(payload.get("password"))

            payload["mf_hash"]=generate_hash()

            serialized = UserProfileWriteSerializer(data=payload)

            if serialized.is_valid(): # check if payload data is correct
                user = serialized.save()
                # user_obj=User.objects.get(email=user)
                user.generate_token()
            else: # There were errors while serializing the payload
                return create_response(create_message([serialized.errors], 102), 400)


            serialized = UserProfileReadSerializer(user)

            return create_response(create_message([serialized.data], 103), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)




    def get_user_details(self, request):
        """Fetch user details with the given email in query params

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Email is mandatory in query params
            # if not get_query_param_or_default(request, "email", None):
            # return create_response(create_message([], 105), 400)
            payload=request.data.copy()
            email=payload.get("email")
            contact_number=payload.get("contact_number")

            # user_type=payload.get("user_type")
            # if  email or contact_number:

            #user get using contact number
            if not email:
                mandatory_keys = [
                "contact_number"

                ]

                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(
                contact_number=payload.get("contact_number")).first()

                # If user does not exist
                if not user:
                    return create_response(create_message([], 104), 404)

            else:
                #user get using email
                mandatory_keys = [
                "email"
            ]

            # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)
                user = User.objects.filter(
                email=payload.get("email")).first()

                # If user does not exist
                if not user:
                    return create_response(create_message([], 104), 404)

            # else:
            #     user=User.objects.all().order_by("created_at")
            #     if not user:
            #          return create_response(create_message([], 452), 404)

            #     if user_type==1:
            #         user=User.objects.filter(user_type=payload.get("user_type")).first()

            #     elif user_type==2:
            #         user=User.objects.filter(user_type=payload.get("user_type")).first()

            #     elif user_type==3:
            #         user=User.objects.filter(user_type=payload.get("user_type")).first()

            #     elif user_type==4:
            #         user=User.objects.filter(user_type=payload.get("user_type")).first()

            #     elif user_type==5:
            #         user=User.objects.filter(user_type=payload.get("user_type")).first()
                # Check if user type id is in the supported user types model
                # elif not int(payload.get("user_type")) in list(UserType.objects.all().values_list("id", flat=True)):
                #     return create_response(create_message([], 101), 400)

            serialized = UserProfileReadSerializer(user)

            return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def update_user_profile(self, request):
        """Update user profile information

        Args:
            request ([WSGI]): [description]

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Get mutable copy of request payload
            payload = request.data.copy()
            email=payload.get("email")

            if not email:
                mandatory_keys=[
                    "contact_number"
                ]
                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

            # Email is mandatory in form data
            # if not payload.get("email", None):
            #     return create_response(create_message([], 105), 400)

                user = User.objects.filter(
                    contact_number=payload.get("contact_number", None)
                ).first()

                # If user does not exist
                #if not user and user.status == 0:
                if not user:
                    return create_response(create_message([], 104), 404)



            else:
                mandatory_keys=[
                    "email"
                ]

                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(
                    email=payload.get("email", None)
                ).first()

                # If user does not exist
                #if not user and user.status_id == 0:
                if not user:
                    return create_response(create_message([], 104), 404)


            # contact number cannot be updated
            payload.pop("contact_number", None)

            # Email cannot be updated
            payload.pop("email", None)
            # Password cannot be updated
            payload.pop("password", None)

            # pop status if status 0 is passed
            payload.pop("status") if payload.get("status", None) and int(payload.get("status")) == 0 else ""

            # Validate payload keys
            status = self.user_helper.validate_update_user_payload(user, payload)
            if type(status).__name__ == "int":
                return create_response(create_message([], status), 400)

            serialized = UserProfileWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(user, serialized.validated_data)
            read_serialized = UserProfileReadSerializer(user)

            return create_response(create_message(read_serialized.data, 108), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def delete_user_profile(self, request):
        """Delete user profile i.e. Change user status to delete"""

        try:

            # Email is mandatory in query params
            # if not get_query_param_or_default(request, "email", None):
            #     return create_response(create_message([], 105), 400)

            payload=request.data.copy()
            email=payload.get("email")

            # delete using contact number
            if not email:
                mandatory_keys=[
                    "contact_number"
                ]
                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(
                    contact_number=payload.get("contact_number",None)
                ).first()

                # If user does not exist
                if not user:
                    return create_response(create_message([], 104), 404)
            else:
                #delete using email
                mandatory_keys=[
                    "email"
                ]
                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(
                    email=payload.get("email",None)
                ).first()

                # If user does not exist
                if not user:
                    return create_response(create_message([], 104), 404)
            # Set user status to deleted
            user.status_id = 0

            # append deleted and uuid at the end of email so the email
            # can be used again for user creation
            user.email = user.email + "deleted" + str(uuid.uuid4())
            user.contact_number = user.contact_number + "deleted" + str(uuid.uuid4())
            user.username = user.username + "deleted" + str(uuid.uuid4())

            user.save()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)

class ResendOtpManagement:


     def resend_otp(self,request):
        try:
            payload=request.data.copy()

            user=User.objects.filter(contact_number=payload.get("contact_number")).first()

            # If user does not exist
            if not user:
                return create_response(create_message([], 104), 404)
            user.generate_token()
            return create_response(create_message([],448),200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)




class VerifyOtpManagement:

    def verify_otp(self, request):
        """Verify users otp """


        try:
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "contact_number",
                "otp"
            ]
            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)

            user = User.objects.filter(contact_number=payload.get("contact_number")).first()
            if not user:
                return create_response(create_message([], 104), 400)

            token=payload.get("otp")

            if user.verify_token(otp=token):
                return create_response(create_message([], 471), 200)
            else:
                return create_response(create_message([], 470), 400)

            # Check code
            # if user.forgot_pwd_email_code != payload.get("code"):
            #     return create_response(create_message([], 211), 400)

            # user.is_forgot_pwd_code_verified = True
            # user.save()

            # return create_response(create_message([], 212), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



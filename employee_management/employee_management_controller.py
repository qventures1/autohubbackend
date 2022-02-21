"""
Controller class for employee management

"""


import uuid

from django.http import request
from employee_management.models import EmployeeProfile,Employee_Profile
from employee_management.serializers import EmployeeProfileReadSerializer,EmployeeProfileWriteSerializer
from user_profile.models import User
from utils.response_utils import create_message, create_response
from user_profile.user_controller import UserProfileController
from service_provider.models import ServiceProvider
from utils.request_utils import get_query_param_or_default
from user_profile.user_helper import UserProfileHelper
from django.db import transaction
from user_profile.serializers import (UserProfileReadSerializer,
                                      UserProfileWriteSerializer)

class EmployeeManagement:
    """Controller class for employee management"""

    user_controller = UserProfileController()
    user_helper = UserProfileHelper()

    def create_employee_profile(self, request):
        """Create an employee profile

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """



        try:
            # Get mutable copy of request.data
            payload = request.data.copy()
            # Mandatory keys in the request payload
            mandatory_keys = [
                "user_type", # The type of user to be created
                "name",
                "email",
                "password",
                "contact_number",
                "service_provider" # Primary key of the Service Provider model, so we can associate this user with service provider
            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)

            # Create User first using existing api in user controller

            response = self.user_controller.create_user(request)

            if response.status_code != 201: # Return the same error response
               return response


            # Get service provider
            sp = ServiceProvider.objects.filter(
                guid=payload.get('service_provider')
            ).first()


            # Create employee profile by relating service provider and user profile
            employee = Employee_Profile.objects.create(

                user=User.objects.get(email=payload.get("email")),
                service_provider = sp)

            serialized = EmployeeProfileReadSerializer(employee)

            return create_response(create_message([serialized.data], 303), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def get_employee_details(self, request):
        """Fetch employee details with the given email in query params

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Email is mandatory in query params
            if not get_query_param_or_default(request, "email", None):
                return create_response(create_message([], 105), 400)

            employee = Employee_Profile.objects.filter(
                user__email=get_query_param_or_default(request, "email", None)
            ).first()


            # If employee does not exist
            if not employee:
                return create_response(create_message([], 104), 404)
            serialized = EmployeeProfileReadSerializer(employee)

            return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)




    def update_employee_profile(self,request):
        """Update Employee profile information

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

            # Email is mandatory in form data
            if not payload.get("email",None):
                return create_response(create_message([], 105),400)

            employee=User.objects.filter(email=payload.get("email",None)).first()
            # If Employee does not exist
            if not employee:
                return create_response(create_message([],104),404)
            # Email cannot be updated
            payload.pop("email",None)
            # Password cannot be updated
            payload.pop("password",None)

            # pop status if status 0 is passed
            payload.pop("status") if payload.get("status",None) and int(payload.get("status")) ==0 else ""

            # Validate payload keys
            status = self.user_helper.validate_update_user_payload(employee, payload)
            if type(status).__name__ == "int":
                return create_response(create_message([], status), 400)

            serialized = UserProfileWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(employee, serialized.validated_data)
                    read_serialized = UserProfileReadSerializer(employee)

            return create_response(create_message(read_serialized.data, 420), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_employee_profile(self, request):
        """Delete Employe profile i.e. Change Employee status to delete"""

        try:

            # Email is mandatory in query params
            if not get_query_param_or_default(request, "email", None):
                return create_response(create_message([], 105), 400)

            employee = User.objects.filter(
                email=get_query_param_or_default(request, "email", None)
            ).first()

            # If Employee does not exist
            if not employee:
                return create_response(create_message([], 104), 404)

            # Set employee status to deleted
            employee.status_id = 0

            # append deleted and uuid at the end of email so the email
            # can be used again for Employee creation
            employee.email = employee.email + "deleted" + str(uuid.uuid4())

            employee.save()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)

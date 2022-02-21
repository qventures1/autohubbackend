"""
Controller class for the authentication app

All business logic related to authentication is contained here

"""

from authentication.auth_helper import AuthHelper
from utils.utils import code_generator
import uuid

from authentication.models import Token
from django.contrib.auth.hashers import check_password, make_password
from user_profile.models import User
from utils.response_utils import create_message, create_response
from utils.request_utils import get_user_from_session,get_user_from_session_contact_number

class AuthController:
    """Controller for authentication related logic"""

    auth_helper = AuthHelper()


    def user_login(self, request):
        """Validate credentials and generate a login token"""

        try:
            payload = request.data.copy()

            email=payload.get("email")

            if not email:
                # Mandatory keys in the request payload
                mandatory_keys = [
                    "contact_number",
                    "password"
                ]

                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(contact_number=payload.get("contact_number")).first()

                if not user: # Invalid contact_number
                    return create_response(create_message([], 468), 401)

            else:
                # Mandatory keys in the request payload
                mandatory_keys = [
                    "email",
                    "password"
                ]

                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(email=payload.get("email")).first()

                if not user: # Invalid email
                    return create_response(create_message([], 203), 401)




            # Check user password
            if not check_password(payload.get("password"), user.password):
                return create_response(create_message([], 203), 401)

            # Search for existing token
            user_token_obj = Token.objects.filter(
                user=user,
                is_valid=True
            ).first()

            if not user_token_obj: # Create new token object in case of first user login
                user_token_obj = Token.objects.create(
                    token=(str(uuid.uuid4()) + str(uuid.uuid4())).replace("-", ""),
                    user=user
                )
            else:
                # Create new token for user
                user_token_obj.token = (str(uuid.uuid4()) + str(uuid.uuid4())).replace("-", "")
                user_token_obj.is_valid = True
                user_token_obj.save()

            response_data = {
                "Token": user_token_obj.token
            }

            return create_response(create_message([response_data], 204), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def user_logout(self, request):
        """Logout the User"""

        try:

            payload = request.data.copy()

            email=payload.get("email")
            if not email:

                # Mandatory keys in the request payload
                mandatory_keys = [
                    "contact_number"
                ]
                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = get_user_from_session_contact_number(request)

                # Login user should match payload contact number
                if user.contact_number != payload.get("contact_number"):
                    return create_response(create_message([], 469), 400)
            else:
                # Mandatory keys in the request payload
                mandatory_keys = [
                    "email"
                ]
                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = get_user_from_session(request)

                # Login user should match payload email
                if user.email != payload.get("email"):
                    return create_response(create_message([], 207), 400)

            user_token_obj = Token.objects.filter(
                user=user
            ).first()

            user_token_obj.is_valid = False
            user_token_obj.save()

            return create_response(create_message([], 206), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def change_password(self, request):
        """Change a User's password"""

        try:

            payload = request.data.copy()
            email=payload.get("email")
            if not email:
                mandatory_keys = [
                    "contact_number",
                    "old_password",
                    "new_password"
                ]

                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(
                    contact_number=payload.get("contact_number")
                ).first()

                if not user:
                    return create_response(create_message([], 104), 400)
            else:

                # Mandatory keys in the request payload
                mandatory_keys = [
                    "email",
                    "old_password",
                    "new_password"
                ]
                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(
                    email=payload.get("email")
                ).first()

                if not user:
                    return create_response(create_message([], 104), 400)

            # Check if old password matches
            if not check_password(payload.get("old_password"), user.password):
                return create_response(create_message([], 208), 400)

            user.password = make_password(payload.get("new_password"))
            user.save()

            return create_response(create_message([], 209), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def forgot_password_send_code(self, request):
        """Send a verification code on user's registered email to verify
        that the user who initiated the forgot password request has access
        to the email they used when registering"""

        try:

            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "contact_number",

            ]
            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)

            user = User.objects.filter(contact_number=payload.get("contact_number")).first()
            if not user:
                return create_response(create_message([], 104), 400)

            #user.forgot_pwd_email_code = code_generator()

            # user.save()

            # TODO: Call helper function to send verification code in email to user
            user.generate_token()

            return create_response(create_message([], 210), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def verify_forgot_pwd_code(self, request):
        """Verify users forgot password code"""


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
                user.is_forgot_pwd_code_verified = True
                user.save()
                return create_response(create_message([], 212), 200)
            else:
                return create_response(create_message([], 211), 400)

            # Check code
            # if user.forgot_pwd_email_code != payload.get("code"):
            #     return create_response(create_message([], 211), 400)

            # user.is_forgot_pwd_code_verified = True
            # user.save()

            # return create_response(create_message([], 212), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def forgot_pwd_code_verified_reset_pwd(self, request):
        """Reset password for email code verified user"""

        try:

            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "contact_number",
                "new_password"
            ]
            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)

            user = User.objects.filter(contact_number=payload.get("contact_number")).first()
            if not user:
                return create_response(create_message([], 104), 400)

            # Check if code is verified
            if not user.is_forgot_pwd_code_verified:
                return create_response(create_message([], 213), 400)

            user.password = make_password(payload.get("new_password"))
            user.save()

            return create_response(create_message([], 214), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


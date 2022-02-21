"""
All views related to the user profile app

"""


from rest_framework.views import APIView
from authentication.auth_controller import AuthController


class UserAuthView(APIView):
    """Auth view for User authentication"""

    authentication_controller = AuthController()

    def post(self, request):
        """Login a User and provide client with a token,
        which they have to send in all the requests to prove
        that they are authenticated users"""

        return self.authentication_controller.user_login(request)


class UserLogoutView(APIView):
    """User Logout View"""

    authentication_controller = AuthController()

    def post(self, request):
        """Logout a User and expire their token"""

        return self.authentication_controller.user_logout(request)


class UserChangePasswordView(APIView):
    """User change password view"""

    authentication_controller = AuthController()

    def post(self, request):
        """Change a users password"""

        return self.authentication_controller.change_password(request)


class UserForgotPasswordCodeView(APIView):
    """User forgot password generate verification code view"""

    authentication_controller = AuthController()

    def post(self, request):
        """Send verification code to users email"""

        return self.authentication_controller.forgot_password_send_code(request)


class UserVerifyForgotPasswordCodeView(APIView):
    """Verify the forgot password email code"""

    authentication_controller = AuthController()

    def post(self, request):
        """Mark forgot password code verified is code matches for user"""

        return self.authentication_controller.verify_forgot_pwd_code(request)


class UserForgotPwdCodeVerifiedResetPwdView(APIView):
    """Reset password for email code verified user"""

    authentication_controller = AuthController()

    def post(self, request):
        """Reset password for code verified user"""

        return self.authentication_controller.forgot_pwd_code_verified_reset_pwd(request)


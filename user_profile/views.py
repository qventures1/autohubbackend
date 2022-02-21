"""
All views related to the user profile app

"""


from user_profile.user_controller import ResendOtpManagement,VerifyOtpManagement
from rest_framework.views import APIView
from user_profile.user_controller import UserProfileController


class UserProfileView(APIView):
    """CRUD View for the User model"""

    user_controller = UserProfileController()

    def post(self, request):
        """Create new User"""

        return self.user_controller.create_user(request)


    def patch(self, request):
        """Update a User"""

        return self.user_controller.update_user_profile(request)


    def get(self, request):
        """Get details of a User"""

        return self.user_controller.get_user_details(request)


    def delete(self, request):
        """Delete/Deactivate a User"""

        return self.user_controller.delete_user_profile(request)


class ResendOtpView(APIView):

    otp_controller_obj=ResendOtpManagement()

    def post(self,request):


        return self.otp_controller_obj.resend_otp(request)


class VerifyOtpView(APIView):
    """verify otp """

    verify_otp_controller_obj=VerifyOtpManagement()

    def post(self,request):


        return self.verify_otp_controller_obj.verify_otp(request)


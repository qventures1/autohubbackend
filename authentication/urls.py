"""
All Urls for the authentication app

"""


from django.urls import path
from authentication import views


urlpatterns = [

    # Login API view
    path("user/login", views.UserAuthView.as_view()),

    # Login API view
    path("user/logout", views.UserLogoutView.as_view()),

    # User change password view for authenticated user
    path("user/change-password", views.UserChangePasswordView.as_view()),

    # User forgot password view
    path("user/forgot-password", views.UserForgotPasswordCodeView.as_view()),

    # Verify forgot password code view
    path("user/forgot-password/verification", views.UserVerifyForgotPasswordCodeView.as_view()),

    # Code verified reset password view
    path("user/forgot-password/reset", views.UserForgotPwdCodeVerifiedResetPwdView.as_view())


]

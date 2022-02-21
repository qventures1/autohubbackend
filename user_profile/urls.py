"""
All Urls for the user profile app

"""


from django.urls import path
from user_profile import views

urlpatterns = [

    # user profile CRUD api view
    path("user", views.UserProfileView.as_view()),
    path("verify-otp", views.VerifyOtpView.as_view()),
    path("resend-otp", views.ResendOtpView.as_view()),


]



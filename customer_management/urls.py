"""
All Urls for the Customer management app

"""


from django.urls import path
from . import views

urlpatterns = [

    # Customer management CRUD api view
    path("profile", views.CustomerProfileView.as_view()),



]

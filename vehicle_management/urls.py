"""
All Urls for the Vehicle management app

"""


from django.urls import path
from . import views

urlpatterns = [

    # vehicle management CRUD api view
    path("vehicle", views.VehicleView.as_view()),
    path("customer-vehicle", views.CustomerVehicleView.as_view())


]


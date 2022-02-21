"""
All Urls for the inventory management app

"""


from django.urls import path
from . import views

urlpatterns = [

    # inventory management CRUD api view
    path("vendor", views.VendorView.as_view())


]


"""
All Urls for the employee management app

"""


from django.urls import path
from . import views

urlpatterns = [

    # employee management CRUD api view
    path("employee", views.EmployeeProfileView.as_view())


]


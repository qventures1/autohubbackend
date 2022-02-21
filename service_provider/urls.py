"""
All urls for the service provider app

"""


from django.urls import path
from service_provider import views


urlpatterns = [

    # Service Provider CRUD view
    path("profile", views.ServiceProvierView.as_view()),

]


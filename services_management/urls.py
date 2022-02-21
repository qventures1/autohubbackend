

from django.urls import path
from . import views

urlpatterns=[
    path("service/",views.ServiceView.as_view()),
    path("service-provider-service/",views.ServiceProviderServicesView.as_view()),
]
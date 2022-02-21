"""
All urls for the delivery cost app

"""


from django.urls import path
from deliveryCost_management import views


urlpatterns = [

    # delivery cost CRUD view
    path("delivery-cost", views.DeliveryCostView.as_view()),


]


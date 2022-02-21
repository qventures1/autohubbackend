"""
All urls for the discounts app

"""


from django.urls import path
from discounts_management import views


urlpatterns = [

    # discounts CRUD view
    path("campaign", views.CampaignView.as_view()),
    path("coupon", views.CouponView.as_view()),


]


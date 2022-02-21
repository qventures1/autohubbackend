"""
All urls for the product app

"""


from django.urls import path
from products_management import views


urlpatterns = [

    # product CRUD view
    path("product-category", views.ProductCategoryView.as_view()),
    path("product", views.ProductsView.as_view()),
    # path("carts",views.AddToCartView.as_view()),

]



from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    # user_profile app urls
    path("autohub/user-profile/", include("user_profile.urls")),

    # authentication app urls
    path("autohub/authentication/", include("authentication.urls")),

    # Service Provider app urls
    path("autohub/service-provider/", include("service_provider.urls")),

   # Customer management app urls
    path("autohub/customer/", include("customer_management.urls")),

    # product management app urls
    path("autohub/product-management/", include("products_management.urls")),

    # Delivery Cost management app urls
    path("autohub/deliveryCost_management/", include("deliveryCost_management.urls")),

    # Discounts management app urls
    path("autohub/discounts-management/", include("discounts_management.urls")),


    # Service Provider Employee management app urls
    path("autohub/service-provider/employee-management/", include("employee_management.urls")),

    # Service Provider Inventory management app urls
    path("autohub/service-provider/inventory-management/", include("inventory_management.urls")),


   # Service Provider Vehicle management app urls
    path("autohub/service-provider/vehicle-management/", include("vehicle_management.urls")),

    path("autohub/services-management/",include("services_management.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

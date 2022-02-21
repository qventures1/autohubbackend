"""
All serializers related to the services app

"""
from vehicle_management.models import Vehicle
from rest_framework.serializers import ModelSerializer
from services_management.models import Services,Service_Provider_Services
from rest_framework.fields import SerializerMethodField
class ServicesWriteSerializer(ModelSerializer):
    """Write serializer for the services model """

    class Meta:
        model=Services
        fields="__all__"


class ServicesReadSerializer(ModelSerializer):
    """Write serializer for the services model """

    class Meta:
        model=Services
        fields="__all__"


class ServiceProviderServicesWriteSerializer(ModelSerializer):
    """Write serializer for the services provider services model """

    class Meta:
        model=Service_Provider_Services
        fields="__all__"


class ServiceProviderServicesReadSerializer(ModelSerializer):
    """Write serializer for the service provider service model """
    vehicle=SerializerMethodField()
    def get_vehicle(self,obj):
        vehicle_list={}
        if obj.vehicle:
            vehicle_list["guid"]=str(obj.vehicle.guid)
            vehicle_list["vehicle_Type"]=str(obj.vehicle.vehicle_Type)
            vehicle_list["vehicle_brand"]=str(obj.vehicle.vehicle_brand)
            # vehicle_list["service_price"]=str(obj.vehicle.service_price)
            return str(vehicle_list)
    class Meta:
        model=Service_Provider_Services
        fields="__all__"
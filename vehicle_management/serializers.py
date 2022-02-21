from django.db.models import fields
from vehicle_management.models import Customer_Vehicle_Details
from rest_framework.serializers import ModelSerializer
from vehicle_management.models import Vehicle

class VehicleSerializer(ModelSerializer):
    """Write serializer for the vehicle types , used in create and update vehicle types"""

    class Meta:
        model=Vehicle
        fields="__all__"



class CustomerVehicleDetailsWriteSerializer(ModelSerializer):

    class Meta:
        model=Customer_Vehicle_Details
        fields="__all__"


class CustomerVehicleDetailsReadSerializer(ModelSerializer):

    class Meta:
        model=Customer_Vehicle_Details
        fields="__all__"
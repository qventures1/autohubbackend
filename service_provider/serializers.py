"""
All serializers related to the service provider app

"""


from rest_framework.fields import SerializerMethodField
from service_provider.models import ServiceProvider
from rest_framework.serializers import ModelSerializer


class ServiceProviderWriteSerializer(ModelSerializer):
    """Write serializer for the ServiceProvider model"""

    class Meta:
        model = ServiceProvider
        fields = "__all__"


class ServiceProviderReadSerializer(ModelSerializer):
    """Read serializer for the ServiceProvider model"""

    guid = SerializerMethodField()

    def get_guid(self, obj):
        if obj.guid:
            return str(obj.guid)

    class Meta:
        model = ServiceProvider
        fields = "__all__"


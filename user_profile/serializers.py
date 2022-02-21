"""
Serializers for the user profile app

"""


from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from user_profile.models import User


class UserProfileWriteSerializer(ModelSerializer):
    """Write serializer for the user profile, used in create and update user profile"""

    class Meta:
        model = User
        fields = "__all__"


class UserProfileReadSerializer(ModelSerializer):
    """Read serializer for the user profile, used where user profile needs to be serialized"""

    guid = SerializerMethodField()

    service_provider = SerializerMethodField()

    def get_guid(self, obj):
        if obj.guid:
            return str(obj.guid)

    def get_service_provider(self, obj):
        if obj.service_provider:
            return str(obj.service_provider.guid)

    class Meta:
        model = User
        fields = "__all__"


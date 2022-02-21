""" Serializers for the vendor  """


from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from inventory_management.models import Vendor
import json

from user_profile.models import User


class VendorWriteSerializer(ModelSerializer):
    """Write serializer for the vendor, used in create and update"""

    class Meta:
        model = Vendor
        fields = "__all__"



class VendorReadSerializer(ModelSerializer):
    """Read serializer for the Vendor, used where vendor profile needs to be serialized"""
    user=SerializerMethodField()
    service_provider = SerializerMethodField()

    def get_user(self,obj):
        user_vendor={}

        if obj.user:
            user_vendor["guid"]=str(obj.user.guid)
            user_vendor["name"]=str(obj.user.name)
            user_vendor["email"]=str(obj.user.email)
            user_vendor["contact_number"]=str(obj.user.contact_number)
            user_vendor["address"]=str(obj.user.address)
            user_vendor["is_origional_manufacturer"]=str(obj.user.is_origional_manufacturer)

            return str(user_vendor)

    def get_service_provider(self, obj):
        if obj.service_provider:
            return str(obj.service_provider.guid)

    class Meta:
        model=Vendor
        fields="__all__"

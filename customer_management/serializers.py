from django.contrib.auth import models
from rest_framework import fields
from customer_management.models import CustomerProfile
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class CustomerProfileWriteSerializer(ModelSerializer):
    """Write serializer for the customer profile, used in create and update customer profile"""

    class Meta:
        model=CustomerProfile
        fields = "__all__"



class CustomerProfileReadSerializer(ModelSerializer):
    """Read serializer for the customer profile, used where customer profile needs to be serialized"""

    user=SerializerMethodField()

    def get_user(self,obj):
        user_list={}

        if obj.user:
            user_list["guid"]=str(obj.user.guid)
            user_list["first_name"]=str(obj.user.first_name)
            user_list["last_name"]=str(obj.user.last_name)
            user_list["contact_number"]=str(obj.user.contact_number)
            user_list["password"]=str(obj.user.password)
            # user_list["language"]=str(obj.user.language)
            # user_list["country"]=str(obj.user.country)

            return str(user_list)



    class Meta:
        model=CustomerProfile
        fields="__all__"





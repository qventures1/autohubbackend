"""
Serializers for the emplyee profile module

"""


from rest_framework.fields import SerializerMethodField
from employee_management.models import Employee_Profile
from rest_framework.serializers import ModelSerializer
import json

from user_profile.models import User


class EmployeeProfileWriteSerializer(ModelSerializer):
    """Write serializer for the employee profile, used in create and update employee profile"""

    class Meta:
        model = Employee_Profile
        fields = "__all__"


class EmployeeProfileReadSerializer(ModelSerializer):
    """Read serializer for the Employee profile, used where Employee profile needs to be serialized"""

    user = SerializerMethodField()

    service_provider = SerializerMethodField()


    def get_user(self, obj):
        l={}
        if obj.user:
            l['guid']=str(obj.user.guid)
            l['username']=str(obj.user.username)
            l['name']=str(obj.user.name)
            l['email']=str(obj.user.email)
            l['contact_number']=str(obj.user.contact_number)
            l['gender']=str(obj.user.gender)
            l['address']=str(obj.user.address)
            return str(l)


    def get_service_provider(self, obj):
        if obj.service_provider:
            return str(obj.service_provider.guid)


    class Meta:
        model = Employee_Profile
        fields = "__all__"
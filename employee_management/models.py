"""
All models related to the employee management

"""


import uuid
from django.db import models
from user_profile.models import User
from service_provider.models import ServiceProvider


class CertificationType(models.Model):
    """Different types of certifications supported in the system"""

    name = models.CharField(max_length=50, null=False, blank=False)
    certification_provider_name = models.CharField(max_length=50, null=True, blank=True)


class EmployeeProfile(models.Model):
    """The Service Provider Employee profile. One to One related with User model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, null=False, blank=False, on_delete=models.CASCADE)


class Employee_Profile(models.Model):
    """The Service Provider Employee profile. One to One related with User model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, to_field="guid", null=True, blank=True, on_delete=models.CASCADE)

class EmployeeCertification(models.Model):
    """Certifications of employees"""

    employee = models.ForeignKey(EmployeeProfile, null=False, blank=False, on_delete=models.CASCADE)
    certification_type = models.ForeignKey(CertificationType, null=False, blank=False, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_at = models.DateTimeField(auto_now_add=True)


class EmployeeWorkStatus(models.Model):
    """Work Statuses of Service Provider Employees"""

    name = models.CharField(max_length=20, null=False, blank=False)


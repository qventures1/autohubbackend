"""
All models directly related to service provider

"""


import uuid
from django.db import models


class ServiceProvider(models.Model):
    """All service providers will be added in this model"""

    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, null=False, blank=False,unique=True)
    email = models.EmailField(null=True, blank=True,unique=True)
    description = models.TextField()
    contact_no = models.CharField(max_length=100, null=True, blank=True,unique=True)
    logo = models.ImageField(upload_to="service_provider_logos")
    latitude=models.CharField(max_length=300, null=True, blank=True)
    longitude=models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

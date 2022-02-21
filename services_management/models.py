from django.db import models
import uuid
from vehicle_management.models import Customer_Vehicle_Details
# Create your models here.

class Services(models.Model):
    """"All services will be added in this model"""

    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False ,unique=True)
    service_name=models.CharField(max_length=200,null=False,blank=False)
    service_price=models.CharField(max_length=50,null=True,blank=True)
    image= models.ImageField(upload_to="services")
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Service_Provider_Services(models.Model):
    """All service provider services will be add in this model"""

    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    service_name=models.CharField(max_length=200,null=False,blank=False)
    service_type=models.CharField(max_length=200,null=False,blank=False)
    duration=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField()
    fixed_price=models.BooleanField(default=False,null=True,blank=True)
    rule_based=models.BooleanField(default=False,null=True,blank=True)
    vehicle=models.ForeignKey(Customer_Vehicle_Details,to_field="guid",on_delete=models.CASCADE)
    service_price=models.CharField(max_length=100,null=True,blank=True)
    relevant_technicians=models.CharField(max_length=100,null=True,blank=True)
    service_on_site=models.BooleanField(default=False,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
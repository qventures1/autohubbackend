from django.db import models
import uuid
# Create your models here.

class Vehicle(models.Model):
    """All Vehicle types and brands added in this model"""
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_brand=models.CharField(max_length=70,blank=True, null=True)
    vehicle_model=models.CharField(max_length=70,null=True,blank=True)
    vehicle_Type=models.CharField(max_length=70,null=True,blank=True)
    year=models.IntegerField()


class Customer_Vehicle_Details(models.Model):
    """All Customer Vehicle details added in this model"""
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_brand=models.CharField(max_length=70,blank=True, null=True)
    vehicle_model=models.CharField(max_length=70,null=True,blank=True)
    vehicle_Type=models.CharField(max_length=70,null=True,blank=True)
    year=models.IntegerField(null=True,blank=True)
    # vehicle=models.ForeignKey(Vehicle,to_field="guid",on_delete=models.CASCADE)
    number_plate=models.CharField(max_length=100,null=True,blank=True,unique=True)
    engine_chesis_number=models.CharField(max_length=100,null=True,blank=True,unique=True)


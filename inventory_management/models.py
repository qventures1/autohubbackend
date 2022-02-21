from django.db import models
from user_profile.models import User
import uuid
from service_provider.models import ServiceProvider

# Create your models here.
class Vendor(models.Model):
    """All Vendor will be added in this model"""

    user=models.OneToOneField(User,to_field="guid",on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, to_field="guid", null=True, blank=True, on_delete=models.CASCADE)

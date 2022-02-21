from django.db import models
from user_profile.models import User
import uuid

# Create your models here.
class CustomerProfile(models.Model):
    """All Customer will be added in this model"""

    user = models.OneToOneField(User,to_field="guid", on_delete=models.CASCADE)



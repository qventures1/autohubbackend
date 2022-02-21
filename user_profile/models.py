"""
All models related to user profile

"""


import uuid
from service_provider.models import ServiceProvider

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import EmailField
from user_profile.send_sms import send_sms
import pyotp
from datetime import datetime, timedelta
import jwt
from autohub_backend.settings import SECRET_KEY
from utils.response_utils import create_message, create_response


class UserStatus(models.Model):
    """Possible user statuses. i.e. Active, Inactive, Deleted etc."""

    name = models.CharField(max_length=30, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)


class UserType(models.Model):
    """Supported user types by the autohub backend. Data is inserted via
    data migration in the common app using `python manage.py data_migrate`
    management command"""

    name = models.CharField(max_length=30, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class User(AbstractUser):
    """User model extending Django's default user model.
    Main User model for the autohub backend. User types e.g. Company, Customer etc
    are maintained using a UserType model through a foreign key relation
    """
    # User identifier
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=200, null=True, blank=True,unique=True)
    email = EmailField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)

    address = models.TextField(null=True,blank=True)
    contact_number = models.CharField(unique=True, max_length=200, null=False, blank=False) # required
    mf_hash = models.CharField(max_length=200,null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)

    image = models.ImageField(upload_to="user_profile_images", null=True,blank=True)
    # Optional Fields
    company_id = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_description = models.CharField(max_length=200, null=True, blank=True)

    cnic = models.CharField(max_length=30, null=True, blank=True)

    user_type = models.ForeignKey(
        UserType, null=False, blank=False, on_delete=models.PROTECT # required
    )

    status = models.ForeignKey(
        UserStatus, null=True, blank=True, on_delete=models.PROTECT
    )

    service_type = models.CharField(max_length=50, null=True, blank=True) # Service Provider
    service_provider = models.ForeignKey(ServiceProvider, null=True, blank=True, on_delete=models.CASCADE) # SP fk
    service_provider_website=models.URLField(max_length=500,null=True,blank=True)
    # Vendor
    is_origional_manufacturer=models.BooleanField(default=False)

    # Forgot password verification code
    forgot_pwd_email_code = models.CharField(max_length=20, null=True, blank=True)

    # Is forgot pwd code verified
    is_forgot_pwd_code_verified = models.BooleanField(default=False)

    # Is user email verified
    is_email_verified = models.BooleanField(default=False)

    #created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Use EMAIL insted of USERNAME
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []




    def generate_token(self):
        """
        Sends the current TOTP token to `self.number`.
        """
        # import pdb
        # pdb.set_trace()
        topt = pyotp.TOTP(self.mf_hash)
        token = topt.now()
        send_sms(contact_number=self.contact_number, otp=token)

    def verify_token(self,otp):
        """
        Verify the provided otp token
        :param otp:
        :return:
        """
        totp = pyotp.TOTP(self.mf_hash)
        if totp.verify(otp, valid_window=1): # otp is valid for one minute
            return True
        else:
            return False

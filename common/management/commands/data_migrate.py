"""
Management command that migrates static data in database tables

"""


from django.core.management.base import BaseCommand
from user_profile.models import UserStatus, UserType


class Command(BaseCommand):
    help = "Data Migrations For Autohub Service"

    def handle(self, *args, **kwargs):


        """Migration Data for UserStatus"""
        # active, inactive and deleted

        delete = UserStatus.objects.get_or_create(
            id=0,
            name="Delete",
            code="D"
        )

        active = UserStatus.objects.get_or_create(
            id=1,
            name="Active",
            code="A"
        )

        inactive = UserStatus.objects.get_or_create(
            id=2,
            name="Inactive",
            code="IA"
        )

        self.stdout.write(self.style.SUCCESS("Data migrated: UserStatus"))


        """Migration Data for UserType"""
        # company, service provider, technician and customer

        company = UserType.objects.get_or_create(
            id=1,
            name="Company",
            code="COM",
            description="This is the Company user profile type"
        )

        service_provider = UserType.objects.get_or_create(
            id=2,
            name="Service Provider",
            code="SP",
            description="This is the Service Provider user profile type"
        )

        service_provider_emp = UserType.objects.get_or_create(
            id=3,
            name="Service Provider Employee",
            code="SPE",
            description="This is the Service Provider Employee user profile type"
        )

        technician = UserType.objects.get_or_create(
            id=4,
            name="Technician",
            code="TECH",
            description="This is the Technician user profile type"
        )

        customer = UserType.objects.get_or_create(
            id=5,
            name="Customer",
            code="CUST",
            description="This is the Customer user profile type"
        )

        self.stdout.write(self.style.SUCCESS("Data migrated: UserType"))


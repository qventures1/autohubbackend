"""
    All views related to the vehicle management
"""

from vehicle_management.vehicle_management_controller import CustomerVehicleManagement
from rest_framework.views  import APIView
from vehicle_management.vehicle_management_controller import VehicleManagement

class VehicleView(APIView):
    """CRUD View for the vehicle model"""


    vehicle_controller = VehicleManagement()

    def post(self, request):
        """Create new vehicle"""

        return self.vehicle_controller.add_vehicle(request)


class CustomerVehicleView(APIView):
    customer_vehicle_controller_obj=CustomerVehicleManagement()
    def post(self,request):

        return self.customer_vehicle_controller_obj.add_customer_vehicle_details(request)


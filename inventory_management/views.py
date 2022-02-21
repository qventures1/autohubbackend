"""
    All views related to the inventory management
"""

from rest_framework.views  import APIView
from inventory_management.inventory_management_controller import InventoryManagement

class VendorView(APIView):
    """CRUD View for the Vendor model"""


    vendor_controller = InventoryManagement()

    def post(self, request):
        """Create new vendor"""

        return self.vendor_controller.creat_vendor(request)


    def get(self,request):
        """show vendor"""

        return self.vendor_controller.show_vendor(request)


    def patch(self,request):
        """update vendor"""

        return self.vendor_controller.update_vendor(request)

    def delete(self, request):
        """Delete/Deactivate a Vendor"""

        return self.vendor_controller.delete_vendor(request)
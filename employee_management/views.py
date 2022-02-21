"""
    All views related to the employee management
"""

from rest_framework.views  import APIView
from employee_management.employee_management_controller import EmployeeManagement

class EmployeeProfileView(APIView):
    """CRUD View for the EmployeeProfile model"""


    employee_controller = EmployeeManagement()

    def post(self, request):
        """Create new employee"""

        return self.employee_controller.create_employee_profile(request)


    def get(self, request):
        """Get details of a employee profile"""

        return self.employee_controller.get_employee_details(request)



    def patch(self,request):
        """Update a Employee Profile"""

        return self.employee_controller.update_employee_profile(request)


    def delete(self, request):
        """Delete/Deactivate a Employee"""

        return self.employee_controller.delete_employee_profile(request)
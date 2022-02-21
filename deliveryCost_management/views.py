"""
All view related to the delivery Cost management

"""
from deliveryCost_management.deliveryCost_management_controller import DeliveryCostMangement
from rest_framework.views import APIView


class DeliveryCostView(APIView):
    """CRUD Api view for the Delivry Cost"""
    delivery_cost_controller=DeliveryCostMangement()

    def post(self,request):

        return self.delivery_cost_controller.add_delivery_cost(request)

    def get(self,request):

        return self.delivery_cost_controller.Show_delivery_cost(request)


    def patch(self,request):

        return self.delivery_cost_controller.update_delivery_cost(request)

    def delete(self,request):

        return self.delivery_cost_controller.delete_delivery_cost(request)

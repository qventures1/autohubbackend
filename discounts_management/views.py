"""
All view related to the discounts management

"""
from discounts_management.discounts_management_controller import CampaignMangement,CouponMangement
from rest_framework.views import APIView


class CampaignView(APIView):
    """CRUD Api view for the campaign"""
    campaign_controller=CampaignMangement()

    def post(self,request):

        return self.campaign_controller.add_campaign(request)

    def get(self,request):

        return self.campaign_controller.Show_campaign(request)


    def patch(self,request):

        return self.campaign_controller.update_campaign(request)

    def delete(self,request):

        return self.campaign_controller.delete_campaign(request)


class CouponView(APIView):
    """CRUD Api view for the Coupon"""

    coupon_controller = CouponMangement()

    def post(self, request):
        """Create a coupon"""

        return self.coupon_controller.add_coupon(request)



    def get(self,request):
        """get coupon"""

        return self.coupon_controller.Show_coupon(request)

    def patch(self,request):
        """update coupon"""

        return self.coupon_controller.update_coupon(request)

    def delete(self,request):
        """delete coupon"""

        return self.coupon_controller.delete_coupon(request)

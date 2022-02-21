from discounts_management.models import Campaign,Coupon
from utils.response_utils import create_message, create_response
from utils.request_utils import get_query_param_or_default
from django.db import transaction
from discounts_management.serializers import CampaignWriteSerializer,CampaignReadSerializer,CouponSerializer


class CampaignMangement:
    """Controller class for Campaign management"""

    def add_campaign(slef,request):
        """create an Campaign """

        try:
            # Get mutable copy of request.data
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "discount_type",
                "min_purchased_items",
                "apply_to",

            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized=CampaignWriteSerializer(data=payload)
            if serialized.is_valid():
                campaign=serialized.save()

            # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized = CampaignReadSerializer(campaign)

            return create_response(create_message([serialized.data],455), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def Show_campaign(self, request):
        """Fetch campaign details """

        try:
            payload=request.data.copy()

            # if get single campaign
            if  payload.get("guid",None):
                campaign=Campaign.objects.filter(guid=payload.get("guid",None)).first()

                if not campaign:
                    return create_response(create_message([], 456), 404)

                serialized =CampaignReadSerializer(campaign)

                return create_response(create_message([serialized.data], 1000), 200)
            else:
                #if show all  campaign
                campaign =Campaign.objects.all().order_by("created_at")

                if not campaign:
                     return create_response(create_message([], 456), 404)

                serialized =CampaignReadSerializer(campaign,many=True)

                return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def update_campaign(self,request):
        """Update Campaign information

        Args:
            request ([WSGI]): [description]

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Get mutable copy of request payload
            payload=request.data.copy()

            # guid is mandatory in form data
            if not payload.get("guid",None):
                return create_response(create_message([], 100),400)

            campaign=Campaign.objects.filter(guid=payload.get("guid",None)).first()

            # If campaign does not exist
            if not campaign:
                return create_response(create_message([],456),404)

            # guid cannot be updated
            payload.pop("guid",None)


            serialized = CampaignWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(campaign, serialized.validated_data)
                    read_serialized = CampaignReadSerializer(campaign)

                return create_response(create_message(read_serialized.data, 457), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_campaign(self, request):
        """Delete campaign by id"""

        try:

            # guid is mandatory in query params
            if not get_query_param_or_default(request, "guid", None):
                return create_response(create_message([], 458), 400)

            campaign = Campaign.objects.filter(
                guid=get_query_param_or_default(request, "guid", None)
            ).first()

            # If campaign does not exist
            if not campaign:
                return create_response(create_message([], 456), 404)

            campaign.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)







class CouponMangement:
    """Controller class for Coupon management"""

    def add_coupon(slef,request):
        """create an Coupon """

        try:
            # Get mutable copy of request.data
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "minimum_cart_amount",
                "discount_rate",

            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized=CouponSerializer(data=payload)
            if serialized.is_valid():
                coupon=serialized.save()

            # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized =CouponSerializer(coupon)

            return create_response(create_message([serialized.data],459), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def Show_coupon(self, request):
        """Fetch coupon details """

        try:
            payload=request.data.copy()

            # if get single coupon
            if  payload.get("guid",None):
                coupon=Coupon.objects.filter(guid=payload.get("guid",None)).first()

                if not coupon:
                    return create_response(create_message([], 460), 404)

                serialized =CouponSerializer(coupon)

                return create_response(create_message([serialized.data], 1000), 200)
            else:
                #if show all  coupon
                coupon =Coupon.objects.all().order_by("created_at")

                if not coupon:
                    return create_response(create_message([], 460), 404)

                serialized =CouponSerializer(coupon,many=True)

                return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def update_coupon(self,request):
        """Update coupon information

        Args:
            request ([WSGI]): [description]

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Get mutable copy of request payload
            payload=request.data.copy()

            # guid is mandatory in form data
            if not payload.get("guid",None):
                return create_response(create_message([], 100),400)

            coupon=Coupon.objects.filter(guid=payload.get("guid",None)).first()

            # If coupon does not exist
            if not coupon:
                return create_response(create_message([],460),404)

            # guid cannot be updated
            payload.pop("guid",None)


            serialized = CouponSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(coupon, serialized.validated_data)
                    read_serialized = CouponSerializer(coupon)

                return create_response(create_message(read_serialized.data, 461), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_coupon(self, request):
        """Delete coupon by id"""

        try:

            # guid is mandatory in query params
            if not get_query_param_or_default(request, "guid", None):
                return create_response(create_message([], 462), 400)

            coupon = Coupon.objects.filter(
                guid=get_query_param_or_default(request, "guid", None)
            ).first()

            # If coupon does not exist
            if not coupon:
                return create_response(create_message([], 460), 404)

            coupon.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)

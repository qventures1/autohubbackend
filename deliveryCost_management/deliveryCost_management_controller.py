from utils.response_utils import create_message, create_response
from utils.request_utils import get_query_param_or_default
from django.db import transaction
from deliveryCost_management.serializers import DeliveryCostSerializer
from deliveryCost_management.models import DeliveryCost



class DeliveryCostMangement:
    """Controller class for delivery cost management"""

    def add_delivery_cost(slef,request):
        """create derivery cost """

        try:
            # Get mutable copy of request.data
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "status",
                "cost_per_delivery",
                "cost_per_product",
                "fixed_cost"

            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized=DeliveryCostSerializer(data=payload)
            if serialized.is_valid():
                delivery=serialized.save()

            # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized = DeliveryCostSerializer(delivery)

            return create_response(create_message([serialized.data],463), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def Show_delivery_cost(self, request):
        """Fetch delivery cost details """

        try:
            payload=request.data.copy()

            # if get single delivery
            if  payload.get("guid",None):
                delivery=DeliveryCost.objects.filter(guid=payload.get("guid",None)).first()

                if not delivery:
                    return create_response(create_message([], 464), 404)

                serialized =DeliveryCostSerializer(delivery)

                return create_response(create_message([serialized.data], 1000), 200)
            else:
                #if show all  delivery cost
                delivery =DeliveryCost.objects.all().order_by("created_at")

                if not delivery:
                     return create_response(create_message([], 464), 404)

                serialized =DeliveryCostSerializer(delivery,many=True)

                return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def update_delivery_cost(self,request):
        """Update delivery cost information

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

            delivery=DeliveryCost.objects.filter(guid=payload.get("guid",None)).first()

            # If delivery does not exist
            if not delivery:
                return create_response(create_message([],464),404)

            # guid cannot be updated
            payload.pop("guid",None)


            serialized = DeliveryCostSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(delivery, serialized.validated_data)
                    read_serialized = DeliveryCostSerializer(delivery)

                return create_response(create_message(read_serialized.data, 465), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_delivery_cost(self, request):
        """Delete delivery cost by id"""

        try:

            # guid is mandatory in query params
            if not get_query_param_or_default(request, "guid", None):
                return create_response(create_message([], 466), 400)

            delivery = DeliveryCost.objects.filter(
                guid=get_query_param_or_default(request, "guid", None)
            ).first()

            # If derivery does not exist
            if not delivery:
                return create_response(create_message([], 467), 404)

            delivery.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



"""
Controller class for Vehicle management
"""

from utils.response_utils import create_message, create_response
from vehicle_management.serializers import VehicleSerializer,CustomerVehicleDetailsWriteSerializer,CustomerVehicleDetailsReadSerializer


class VehicleManagement:
    """controller class for the vehicle management"""

    def add_vehicle(self,requet):
        """create a vehicle

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """


        try:
            # Get mutable copy of request.data
            payload=requet.data.copy()

            # Mandatory keys in the request payload
            mandatory_key=[
                "vehicle_brand",
                "vehicle_model",
                "vehicle_Type",
                "year"
            ]

             # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_key):
                return create_response(create_message(mandatory_key,100),400)

            serialized=VehicleSerializer(data=payload)
            if serialized.is_valid():
                serialized.save()
            # # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized=VehicleSerializer(payload)

            return create_response(create_message([serialized.data],438),201)


        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)

class CustomerVehicleManagement:
    def add_customer_vehicle_details(self,requet):
        """add customer vehicle details

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """


        try:
            # Get mutable copy of request.data
            payload=requet.data.copy()

            # Mandatory keys in the request payload
            mandatory_key=[
                "vehicle_brand",
                "vehicle_model",
                "vehicle_Type",
                "year",
                "number_plate",
                "engine_chesis_number",
            ]

             # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_key):
                return create_response(create_message(mandatory_key,100),400)

            serialized=CustomerVehicleDetailsWriteSerializer(data=payload)
            if serialized.is_valid():
                serialized.save()
            # # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized=CustomerVehicleDetailsReadSerializer(payload)

            return create_response(create_message([serialized.data],439),201)


        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)

"""
Controller class for products management

"""


import uuid

from django.http import request
from products_management.models import Category
from products_management.serializers import ProductsCategoryReadSerializer, ProductsCategoryWriteSerializer
from products_management.models import Cart
from products_management.serializers import CartSerializer
from rest_framework import serializers
from utils.response_utils import create_message, create_response
from utils.request_utils import get_query_param_or_default
from django.db import transaction
from products_management.serializers import (ProductsWriteSerializer,ProductsReadSerializer)
from products_management.models import Products


class CategoryMangement:
    """Controller class for products category management"""

    def add_category(slef,request):
        """create an category """

        try:
            # Get mutable copy of request.data
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "title"

            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized=ProductsCategoryWriteSerializer(data=payload)
            if serialized.is_valid():
                category=serialized.save()

            # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized = ProductsCategoryReadSerializer(category)

            return create_response(create_message([serialized.data],450), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def Show_Category(self, request):
        """Fetch all products category details """

        try:
            payload=request.data.copy()
            # if get single product
            if  payload.get("guid",None):
                category=Category.objects.filter(guid=payload.get("guid",None)).first()

                if not category:
                    return create_response(create_message([], 452), 404)

                serialized = ProductsCategoryReadSerializer(category)

                return create_response(create_message([serialized.data], 1000), 200)
            else:
                #if show all  products
                category =Category.objects.all().order_by("created_at")

                if not category:
                     return create_response(create_message([], 452), 404)

                serialized = ProductsCategoryReadSerializer(category,many=True)

                return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def update_Category(self,request):
        """Update product category information

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

            category=Category.objects.filter(guid=payload.get("guid",None)).first()
            # If category does not exist
            if not category:
                return create_response(create_message([],452),404)
            # guid cannot be updated
            payload.pop("guid",None)


            serialized = ProductsCategoryWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(category, serialized.validated_data)
                    read_serialized = ProductsCategoryReadSerializer(category)

            return create_response(create_message(read_serialized.data, 453), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_category(self, request):
        """Delete product category by id"""

        try:

            # guid is mandatory in query params
            if not get_query_param_or_default(request, "guid", None):
                return create_response(create_message([], 454), 400)

            category = Category.objects.filter(
                guid=get_query_param_or_default(request, "guid", None)
            ).first()

            # If product category does not exist
            if not category:
                return create_response(create_message([], 452), 404)

            category.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)

class ProductsManagement:
    """Controller class for products management"""

    def Add_product(self, request):
        """Create an product

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """



        try:
            # Get mutable copy of request.data
            payload = request.data.copy()
            # Mandatory keys in the request payload
            mandatory_keys = [
                "title",
                "image",
                "price",

            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized=ProductsWriteSerializer(data=payload)
            if serialized.is_valid():
                product=serialized.save()

            # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized = ProductsReadSerializer(product)

            return create_response(create_message([serialized.data],432), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



    def Show_products(self, request):
        """Fetch all products details

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:


            payload=request.data.copy()

            # if get single product
            if  payload.get("guid",None):

                product=Products.objects.filter(guid=payload.get("guid",None)).first()

                if not product:
                    return create_response(create_message([], 433), 404)

                serialized = ProductsReadSerializer(product)

                return create_response(create_message([serialized.data], 1000), 200)
            else:
                products =Products.objects.all().order_by("created_at")


            if not products:
                return create_response(create_message([], 433), 404)

            serialized = ProductsReadSerializer(products,many=True)

            return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


    def update_product(self,request):
        """Update product information

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

            product=Products.objects.filter(guid=payload.get("guid",None)).first()
            # If guid does not exist
            if not product:
                return create_response(create_message([],433),404)
            # guid cannot be updated
            payload.pop("guid",None)


            serialized = ProductsWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(product, serialized.validated_data)
                    read_serialized = ProductsReadSerializer(product)

            return create_response(create_message(read_serialized.data, 441), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)],1002),500)



    def delete_product(self, request):
        """Delete product by id"""

        try:

            # guid is mandatory in query params
            if not get_query_param_or_default(request, "guid", None):
                return create_response(create_message([], 440), 400)

            product = Products.objects.filter(
                guid=get_query_param_or_default(request, "guid", None)
            ).first()

            # If product does not exist
            if not product:
                return create_response(create_message([], 433), 404)

            product.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)



# class Add_To_Cart_Management:
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

#     def add_to_cart(self,request):

#         cart = self.queryset
#         try:
#             payload=request.data.copy()

#             print(payload)
#             product=Products.objects.filter(guid=payload.get("guid",None)).first()
#             print(product)
#             # if product does not exist
#             if not product:
#                 return create_response(create_message([],433),404)

#             quantity=int(payload.get("quantity"))
#             print(quantity)

#             # Disallow adding to cart if available inventory is not enough
#             if product.available_products <=0 or product.available_products - quantity < 0:
#                 return create_response(create_message([],449),404)



#             existing_cart_item=CartItem.objects.filter(cart=cart,product=product).first()
#             # before creating a new cart item check if it is in the cart already
#             # and if yes increase the quantity of that item

#             if existing_cart_item:
#                 existing_cart_item.quantity += quantity
#                 existing_cart_item.save()
#             else:
#                 new_cart_item = CartItem(cart=cart, product=product, quantity=quantity)
#                 new_cart_item.save()

#             # return the updated cart to indicate success
#             serializer=CartSerializer(data=cart)
#             return create_response(create_message([serializer.data],450),201)


#         except Exception as ex:
#             print(ex)
#             return create_response(create_message([str(ex)], 1002), 500)








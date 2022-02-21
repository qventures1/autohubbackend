from products_management.models import Category
from products_management.models import Cart
from customer_management.serializers import CustomerProfileReadSerializer
from rest_framework import serializers
from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from products_management.models import Products
from rest_framework.fields import SerializerMethodField


class ProductsCategoryWriteSerializer(ModelSerializer):
    """Write serializer for the products category, used in create and update category"""

    class Meta:
        model=Category
        fields = "__all__"


class ProductsCategoryReadSerializer(ModelSerializer):
    """Read serializer for the products category, used where products category needs to be serialized"""

    class Meta:
        model=Category
        fields = "__all__"



class ProductsWriteSerializer(ModelSerializer):
    """Write serializer for the products, used in create and update products"""

    class Meta:
        model=Products
        fields = "__all__"



class ProductsReadSerializer(ModelSerializer):
    """Read serializer for the products, used where products needs to be serialized"""

    category=SerializerMethodField()


    def get_category(self,obj):
        if obj.category:
            return str(obj.category.guid)



    class Meta:
        model=Products
        fields="__all__"

class CartSerializer(ModelSerializer):
    """Serializer for the Cart model."""
    # customer = CustomerProfileReadSerializer(read_only=True)
    # items=serializers.StringRelatedField(many=True)

    class Meta:
        model=Cart
        fields=[

            'id', 'user', 'product', 'quantity', 'created_at', 'updated_at'
        ]



# class CartItemSerializer(ModelSerializer):
#     """Serializer for the CartItem model."""

#     cart=CartSerializer(read_only=True)
#     product=ProductsReadSerializer(read_only=True)

#     class Meta:
#         model=CartItem
#         fields=(
#             'guid','cart','product','quantity'
#         )


# class OrderSerializer(ModelSerializer):
#     """Serializer for the Order model."""

#     customer=CustomerProfileReadSerializer(read_only=True)
#      # used to represent the target of the relationship using its __unicode__ method
#     order_items = serializers.StringRelatedField(many=True, required=False)

#     class Meta:
#         model = Order
#         fields = (
#             'guid', 'customer', 'total', 'created_at', 'updated_at', 'order_items'
#         )




# class OrderItemSerializer(ModelSerializer):
#     """Serializer for the OrderItem model."""

#     order=OrderSerializer(read_only=True)
#     product=ProductsReadSerializer(read_only=True)

#     class Meta:
#         model=OrderItem
#         fields=(
#             'guid', 'order', 'product', 'quantity'
#         )
from deliveryCost_management.models import DeliveryCost
from rest_framework.serializers import ModelSerializer

class DeliveryCostSerializer(ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['guid', 'status', 'cost_per_delivery', 'cost_per_product', 'fixed_cost', 'created_at', 'updated_at']

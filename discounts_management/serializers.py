from rest_framework.serializers import ModelSerializer
from .models import Campaign, Coupon
from rest_framework.fields import SerializerMethodField

class CampaignWriteSerializer(ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['guid', 'discount_type', 'discount_rate', 'discount_amount', 'min_purchased_items',
                  'apply_to', 'target_product', 'target_category', 'created_at', 'updated_at']



class CampaignReadSerializer(ModelSerializer):
    target_category=SerializerMethodField()
    target_product=SerializerMethodField()


    def get_target_product(self,obj):
        if obj.target_product:
            return str(obj.target_product.guid)


    def get_target_category(self,obj):
        if obj.target_category:
            return str(obj.target_category.guid)
    class Meta:
        model = Campaign
        fields = ['guid', 'discount_type', 'discount_rate', 'discount_amount', 'min_purchased_items',
                  'apply_to', 'target_product', 'target_category', 'created_at', 'updated_at']


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['guid', 'minimum_cart_amount', 'discount_rate', 'created_at', 'updated_at']
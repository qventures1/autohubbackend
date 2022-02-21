from django.db import models
import uuid
from products_management.models import Products,Category

# Create your models here.

class Campaign(models.Model):
    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    discount_type = models.CharField(max_length=6,
                                     choices=(('Amount', 'amount'), ('Rate', 'rate')),
                                     default="rate",
                                     null=False,
                                     blank=False)
    discount_rate = models.IntegerField(null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    min_purchased_items = models.IntegerField(null=False,blank=False)
    apply_to = models.CharField(max_length=8,
                                choices=(('Product', 'product'), ('Category', 'category')),
                                default="product",
                                null=False,blank=False)
    target_product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    target_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.guid,
                                                                   self.discount_type,
                                                                   self.discount_rate,
                                                                   self.discount_amount,
                                                                   self.min_purchased_items,
                                                                   self.apply_to,
                                                                   self.target_product,
                                                                   self.target_category,
                                                                   self.created_at,
                                                                   self.updated_at)


class Coupon(models.Model):
    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    minimum_cart_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False,blank=False)
    discount_rate = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.guid,
                                          self.minimum_cart_amount,
                                          self.discount_rate,
                                          self.created_at,
                                          self.updated_at)
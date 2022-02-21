from django.db import models

# Create your models here.

import uuid
from autohub_backend import settings
from user_profile.models import User

class Category(models.Model):
    """All Products category will be added in this model"""
    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255, null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_category_guid = models.UUIDField(null=True, blank=True)
    def __str__(self):
        return "{} - {} - {} - {} -{}".format(self.guid,
                                          self.title,
                                          self.parent_category_guid,
                                          self.created_at,
                                          self.updated_at)


class Products(models.Model):
    """All Products will be added in this model"""

    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category = models.ForeignKey(Category,to_field="guid", on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100,null=False,blank=False)
    image=models.ImageField(upload_to="products_images")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_products = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.guid,
                                               self.category,
                                               self.image,
                                               self.title,
                                               self.price,
                                               self.available_products,
                                               self.created_at,
                                               self.updated_at)


class Cart(models.Model):
    """A model that contains data for a shopping cart."""
    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(
        User,
        related_name='cart',
        on_delete=models.SET_NULL,
        to_field="guid",
        null=True,
        blank=True
    )
    product=models.ForeignKey(Products,to_field="guid",related_name="items",on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} -{} - {} - {}".format(self.guid,
                                                    self.user,
                                                    self.product,
                                                    self.quantity,
                                                    self.created_at,
                                                    self.updated_at)


# class CartItem(models.Model):
#     """A model that contains data for an item in the shopping cart."""
#     guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     cart=models.ForeignKey(Cart,to_field="guid",null=True,blank=True,related_name="items",on_delete=models.CASCADE)
#     product=models.ForeignKey(Products,to_field="guid",related_name="items",on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1,null=True,blank=True)

#     def __unicode__(self):
#         return '%s: %s' % (self.product.title, self.quantity)


# class Order(models.Model):

#     guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     customer=models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         related_name="orders",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         to_field="guid"
#     )
#     total=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class OrderItem(models.Model):
#     """A model that contains data for an item in an order."""

#     guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     order=models.ForeignKey(
#         Order,
#         related_name='order_items',
#         on_delete=models.CASCADE,
#         to_field="guid"
#     )
#     product=models.ForeignKey(
#         Products,
#         related_name='order_items',
#         to_field="guid",
#         on_delete=models.CASCADE
#     )
#     quantity=models.PositiveIntegerField(null=True,blank=True)


#     def __unicode__(self):
#         return '%s: %s' % (self.product.title, self.quantity)

from django.db import models
import uuid
# Create your models here.
class DeliveryCost(models.Model):
    guid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status = models.CharField(max_length=7,
                              choices=(('Active', 'active'), ('Passive', 'passive')),
                              default="passive",
                              null=False,blank=False)
    cost_per_delivery = models.DecimalField(max_digits=10, decimal_places=2, null=False,blank=False)
    cost_per_product = models.DecimalField(max_digits=10, decimal_places=2, null=False,blank=False)
    fixed_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.guid,
                                                    self.status,
                                                    self.cost_per_delivery,
                                                    self.cost_per_product,
                                                    self.fixed_cost,
                                                    self.created_at,
                                                    self.updated_at)

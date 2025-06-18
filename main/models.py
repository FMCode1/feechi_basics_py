from django.db import models

# Create your models here.
class Inventory(models.Model):
    product_name = models.TextField(max_length=50)
    product_price = models.FloatField(null=False, blank=False)

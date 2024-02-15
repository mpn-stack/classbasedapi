from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count =models.IntegerField(default=1)
    expire_data = models.DateTimeField()
    register_date = models.DateTimeField(default=timezone.now)

from rest_framework import serializers
from .models import Product
from django.utils import timezone
from datetime import timedelta
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= '__all__'

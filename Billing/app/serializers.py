from .models import BillingModel
from rest_framework import serializers


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingModel
        fields = ['category', 'item', 'quantity', 'price', 'date', 'time']

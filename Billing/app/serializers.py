from .models import BillingModel
from rest_framework import serializers

# Here I have inherited ModelSerializer and defined below class which is responsible for serialization and de-serialization.
class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingModel
        fields = ['category', 'item', 'quantity', 'price', 'date', 'time']

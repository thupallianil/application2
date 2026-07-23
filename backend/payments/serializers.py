from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client', read_only=True)
    class Meta:
        model = Payment
        fields = ['id', 'payment_id', 'client', 'client_name', 'amount', 'date', 'method']

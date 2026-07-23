from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client', read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice', 'client', 'client_name', 'amount', 'status']

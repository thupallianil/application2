from rest_framework import serializers
from .models import Quotation


class QuoteSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.client", read_only=True)

    class Meta:
        model = Quotation
        fields = [
            "id",
            "quotation_id",
            "client",
            "client_name",
            "amount",
            "status",
        ]
from rest_framework import viewsets
from .models import Quotation
from .serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuoteSerializer
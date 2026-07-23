from django.db import models
from backend.clients.models import Client


class Payment(models.Model):
    payment_id = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    method = models.CharField(
        max_length=50,
        choices=[
            ("Bank Transfer", "Bank Transfer"),
            ("Credit Card", "Credit Card"),
            ("Cash", "Cash"),
        ],
    )

    def __str__(self):
        return self.payment_id
from django.db import models
from backend.clients.models import Client


class Invoice(models.Model):
    invoice = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="invoices"
    )
    amount = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Paid", "Paid"),
            ("Pending", "Pending"),
        ],
    )

    def __str__(self):
        return self.invoice
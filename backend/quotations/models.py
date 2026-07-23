from django.db import models
from backend.clients.models import Client


class Quotation(models.Model):
    quotation_id = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Accepted", "Accepted"),
            ("Pending", "Pending"),
            ("Rejected", "Rejected"),
        ],
    )

    def __str__(self):
        return self.quotation_id
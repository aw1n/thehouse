from django.db import models

from roommate.models import Roommate
from thehouse.models import House

class Transaction(models.Model):
    payer = models.ForeignKey(Roommate)
    house = models.ForeignKey(House)

    totalAmount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    date_created = models.DateTimeField()

class DebtItem(models.Model):
    debtor = models.ForeignKey(Roommate)
    
    paid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    date_paid = models.DateTimeField()

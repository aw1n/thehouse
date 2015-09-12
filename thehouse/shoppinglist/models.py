from django.db import models

from roommate.models import Roommate
from thehouse.models import House

class ShoppingItem(models.Model):
    priorities = (
        ('low', 'Low'),
        ('med', 'Medium'),
        ('high', 'High'),
    )
    
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=priorities)

    created_by = models.ForeignKey(Roommate)
    house = models.ForeignKey(House)

    date_created = models.DateTimeField()

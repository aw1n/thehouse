from django.db import models

from roommate.models import Roommate
from thehouse.models import House

class Chore(models.Model):
    priorities = (
        ('low', 'Low'),
        ('med', 'Medium'),
        ('high', 'High'),
    )

    assignee = models.ForeignKey(Roommate, null=True)
    house = models.ForeignKey(House)

    priority = models.CharField(max_length=10, choices=priorities)
    description = models.TextField()

    date_created = models.DateTimeField()
    date_due = models.DateTimeField()
    
    repeated = models.BooleanField(default=True)
    repeat_period = models.DurationField()


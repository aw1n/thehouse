from django.db import models

from roommate.models import Roommate

class Event(models.Model):
    roommate = models.ForeignKey(Roommate)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    description = models.TextField()

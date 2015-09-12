from django.db import models

from roommate.models import Roommate

class House(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    roommates = models.ManyToManyField(Roommate)

    date_created = models.DateTimeField()

class Announcement(models.Model):
    message = models.TextField()
    house = models.ForeignKey(House)
    roommate = models.ForeignKey(Roommate, null=True)

    date_created = models.DateTimeField()


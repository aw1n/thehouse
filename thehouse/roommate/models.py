from django.db import models
from django.contrib.auth.models import User

class Roommate(models.Model):
    user = models.OneToOneField(User)

class Alert(models.Model):
    message = models.TextField()
    roommate = models.ForeignKey(Roommate)

    date_created = models.DateTimeField()

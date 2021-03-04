from django.db import models

# Create your models here.

class subscription(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """

    low_light = models.BooleanField()
    low_humidity = models.BooleanField()
    pet_friendly = models.BooleanField()


from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Subscription(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='subscriptions')

    low_light = models.BooleanField()
    low_humidity = models.BooleanField()
    pet_friendly = models.BooleanField()


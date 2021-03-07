from django.db import models
from profiles.models import UserProfile
from checkout.models import Order
from products.models import Product

# Create your models here.


class Subscription(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='subscription')
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='subscription')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)

    low_light = models.BooleanField()
    low_humidity = models.BooleanField()
    pet_friendly = models.BooleanField()



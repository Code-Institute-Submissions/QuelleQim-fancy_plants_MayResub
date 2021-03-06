from django import forms
# from .models import UserProfile
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription

    """
    A user subscription model for maintaining default
    subscription options
    """
    low_light = forms.BooleanField()
    low_humidity = forms.BooleanField()
    pet_friendly = forms.BooleanField()


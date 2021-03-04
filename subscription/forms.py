from django import forms


class SubscriptionForm(forms.ModelForm):
    """
    A user profile model for maintaining default
    delivery information and order history
    """

    low_light = forms.BooleanField()
    low_humidity = forms.BooleanField()
    pet_friendly = forms.BooleanField()

    class Meta:
        model = subscription

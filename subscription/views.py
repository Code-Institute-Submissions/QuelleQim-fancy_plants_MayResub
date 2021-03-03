from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

# Create your views here.


def view_subscriptions(request):
    """ A view that views the subscription page """

    return render(request, 'subscription/subscription.html')

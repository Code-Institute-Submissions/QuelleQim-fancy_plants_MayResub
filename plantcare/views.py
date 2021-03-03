from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

# Create your views here.


def view_plant_care(request):
    """ A view that views the plant care page """

    return render(request, 'plantcare/plantcare.html')


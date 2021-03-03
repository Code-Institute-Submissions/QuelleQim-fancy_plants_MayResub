from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

# Create your views here.


def view_plant_care(request):
    """ A view that views the plant care page """

    return render(request, 'plantcare/plantcare.html')


# def water_care(request):
#     """ A view that views the watering plant care page """

#     return render(request, 'plantcare/water.html')


# def sun_care(request):
#     """ A view that views the sun plant care page """

#     return render(request, 'plantcare/sun.html')


# def earth_care(request):
#     """ A view that views the earth plant care page """

#     return render(request, 'plantcare/earth.html')


# def air_care(request):
#     """ A view that views the air plant care page """

#     return render(request, 'plantcare/air.html')

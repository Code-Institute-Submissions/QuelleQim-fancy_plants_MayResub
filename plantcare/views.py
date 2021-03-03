from django.shortcuts import render

# Create your views here.


def plant_care(request):
    """ A view to return the plant care page """

    return render(request, 'plantcare/plantcare.html')

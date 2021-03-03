from django.shortcuts import render

# Create your views here.


def plantcare(request):
    """ A view to return the index page """

    return render(request, 'plantcare/plantcare.html')

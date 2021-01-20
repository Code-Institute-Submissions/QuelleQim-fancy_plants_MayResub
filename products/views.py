from django.shortcuts import render
from .model import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, icluding sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

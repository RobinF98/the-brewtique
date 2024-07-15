from django.shortcuts import render
from .models import Category, Product

# Create your views here.


def products(request):
    """ all products view """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products/products.html", context)

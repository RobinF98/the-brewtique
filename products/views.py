from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Q
from .models import Category, Product

# Create your views here.


def products(request):
    """ all products view """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            # return all products page if no search query is entered
            if not query:
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):
    """ View to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "products/product_detail.html", context)

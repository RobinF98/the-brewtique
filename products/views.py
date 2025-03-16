from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Q
from .models import Category, Product

# Create your views here.


def products(request):
    """ all products view """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:

        if 'sort' in request.GET:
            sort = request.GET['sort'].split('-')
            direction = sort[1]
            sortkey = sort[0]

            if direction == 'desc':
                sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            # return all products page if no search query is entered
            if not query:
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'category': category,
        'sorting': sort,
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):
    """ View to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "products/product_detail.html", context)

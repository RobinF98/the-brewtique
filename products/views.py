from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Q

from wishlist.models import Wishlist, WishlistItem
from .models import Category, Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def products(request):
    """ all products view """

    products = Product.objects.all()
    query = None
    category = None
    sort = None

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
        'sort': sort,
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):
    """ View to show product details """

    product = get_object_or_404(Product, pk=product_id)
    in_wishlist = None

    # Check if product is in wishlist
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.get_or_create(user=request.user)
        in_wishlist = WishlistItem.objects.filter(wishlist=wishlist[0], product=product).exists()

    context = {
        'product': product,
        'in_wishlist': in_wishlist,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    '''Delete a product from the store'''

    if not request.user.is_superuser:
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))

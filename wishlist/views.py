from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from products.models import Product

from .models import Wishlist, WishlistItem


@login_required
def view_wishlist(request):
    '''Create and/or view wishlist'''
    wishlist = Wishlist.objects.get_or_create(user=request.user)[0]
    itemQuery = WishlistItem.objects.filter(wishlist=wishlist)
    if itemQuery.exists():
        wishlistItems = WishlistItem.objects.filter(wishlist=wishlist)
    else:
        wishlistItems = {}

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlistItems,
    }
    return render(request, template, context,)


@login_required
def add_to_wishlist(request, product_id):
    '''Add product to wishlist'''
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    # add product if it is not already in wishlist
    if not WishlistItem.objects.filter(product=product_id).exists():
        WishlistItem.objects.create(wishlist=wishlist[0], product=product)
        return redirect(reverse('product_detail', args=[product_id]))


def remove_from_wishlist(request, product_id, redir):
    '''Remove product from wishlist'''
    # check if product is actually in the wishlist, and delete
    if WishlistItem.objects.filter(product=product_id).exists():
        WishlistItem.objects.filter(product=product_id).delete()
    print(request.path)
    if redir == 'prd':
        return redirect(reverse('product_detail', args=[product_id]))
    else:
        return redirect(reverse('wishlist'))

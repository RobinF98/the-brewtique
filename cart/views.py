from django.shortcuts import redirect, render, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    ''' View to render cart contents '''

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    ''' Add quantity of specified product to the cart '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Check if item is in cart, and update qty / add item as necessary
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    ''' Add quantity of specified product to the cart '''

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    '''Remove specified item from the cart'''
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

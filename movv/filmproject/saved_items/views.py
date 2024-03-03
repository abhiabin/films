from filmapp.models import film
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404


def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart






def add_cart(request,film_id):
    Product=film.objects.get(id=film_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save(),
    try:
        cart_item=CartItem.objects.get(Product=Product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            Product=Product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('saved_items:cart_detail')
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            counter +=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'saveditem.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,film_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    Product=get_object_or_404(film,id=film_id)
    cart_item=CartItem.objects.get(Product=Product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('saved_items:cart_detail')

def full_remove(request,film_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    Product = get_object_or_404(film, id=film_id)
    cart_item = CartItem.objects.get(Product=Product, cart=cart)
    cart_item.delete()
    return redirect('saved_items:cart_detail')





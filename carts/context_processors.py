from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    if 'admin' in request.path:
        return {}
    else:
        cart_count = 0
        # if request.user.is_authenticated:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
        return {'cart_count': cart_count}
from decimal import Decimal, ROUND_DOWN
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available
    when rendering every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    subtotal = 0
    product_count = 0
    shipping = Decimal('1.20').quantize(Decimal('.01'), rounding=ROUND_DOWN)

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        price_by_quantity = Decimal(quantity) * Decimal(product.price)
        product_count += quantity
        subtotal += Decimal(quantity) * Decimal(product.price)
        cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'item_total': price_by_quantity})

    # Shipping and total need to be outside the loop to avoid repeated additions that aren't necessary
    shipping *= product_count
    total = (subtotal + shipping)

    return {'cart_items': cart_items, 'subtotal': subtotal, 'shipping': shipping, 'total': total, 'product_count': product_count}
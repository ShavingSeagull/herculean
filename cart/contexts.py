from decimal import Decimal, ROUND_DOWN
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages
from products.models import Product
from promocodes.models import PromoCode


def cart_contents(request):
    """
    Ensures that the cart contents are available
    when rendering every page. Also utilises the built-in
    Decimal function to handle the decimal numbers required for
    displaying monetary amounts. Quantize ensures the amounts
    remain human readable.
    """

    cart = request.session.get('cart', {})
    code = request.POST.get('discount')
    now = timezone.now()

    cart_items = []
    discount = Decimal('0').quantize(Decimal('.01'))
    subtotal = Decimal('0').quantize(Decimal('.01'))
    product_count = 0
    shipping = Decimal('1.20').quantize(Decimal('.01'))

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        price_by_quantity = Decimal(quantity) * Decimal(product.price)
        product_count += quantity
        subtotal += Decimal(quantity) * Decimal(product.price)
        cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'item_total': price_by_quantity})

    if code:
        try:
            promocode = PromoCode.objects.get(code__iexact=code,
                                              start_date__lte=now,
                                              expiry_date__gte=now,
                                              active=True)

            discount = (promocode.discount * subtotal) / Decimal(100)
            subtotal -= Decimal(discount).quantize(Decimal('.01'))

        except PromoCode.DoesNotExist:
            messages.error(request, "Promo Code is invalid")

        #request.session['promocode'] = promocode

    # Shipping and total need to be outside the loop to avoid repeated additions that aren't necessary
    shipping *= product_count
    total = Decimal(subtotal + shipping).quantize(Decimal('.01'))

    return {'cart_items': cart_items, 'subtotal': subtotal, 'shipping': shipping, 'total': total, 'discount': discount, 'product_count': product_count}

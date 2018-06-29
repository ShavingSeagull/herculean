from decimal import Decimal
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from products.models import Product
from promocodes.models import PromoCode
import stripe

stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            if request.user.is_authenticated:
                order.email = request.user.email
            else:
                email = request.POST.get('order-email')
                order.email = email

            order.save()

            now = timezone.now()
            cart = request.session.get("cart", {})
            code = request.session.get('discount', {})
            discount_total = Decimal(0)
            subtotal = Decimal('0').quantize(Decimal('.01'))
            shipping = Decimal('1.20').quantize(Decimal('.01'))
            product_count = 0

            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                category = product.choice
                price_by_quantity = Decimal(quantity) * Decimal(product.price)
                subtotal += price_by_quantity

                if code:
                    try:
                        promocode = PromoCode.objects.get(code__iexact=code,
                                                          start_date__lte=now,
                                                          expiry_date__gte=now,
                                                          active=True)

                        # Promo Codes can target specific product groups, like Protein products, or all products
                        # This checks if the Code type matches the product type, or whether it targets all products
                        if promocode.product_type == category or promocode.product_type == 'all':
                            discount = Decimal((promocode.discount * price_by_quantity) / Decimal(100)).quantize(Decimal('.01'))
                            discount_total += discount

                    except PromoCode.DoesNotExist:
                        messages.error(request, "Promo Code is invalid")

                product_count += quantity

                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            shipping *= product_count
            total = Decimal(subtotal - discount_total + shipping).quantize(Decimal('.01'))

            if request.user.is_authenticated and code:
                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),
                        currency="GBP",
                        description='Order #: %s' % order.id,
                        card=payment_form.cleaned_data['stripe_id'],
                        metadata={
                            'Email': request.user.email,
                            'Full Name': order.full_name,
                            'Promo Code': code,
                        },
                    )
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined")
            elif request.user.is_authenticated:
                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),
                        currency="GBP",
                        description='Order #: %s' % order.id,
                        card=payment_form.cleaned_data['stripe_id'],
                        metadata={
                            'Email': request.user.email,
                            'Full Name': order.full_name,
                        },
                    )
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined")
            else:
                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),
                        currency="GBP",
                        description='Order #: %s' % order.id,
                        card=payment_form.cleaned_data['stripe_id'],
                        metadata={
                            'Email': request.POST.get('order-email'),
                            'Full Name': order.full_name,
                        },
                    )
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined")

            if customer.paid:
                request.session['cart'] = {}
                request.session['order_number'] = order.id
                try:
                    del request.session['discount']
                except KeyError:
                    pass
                return redirect(reverse('order-success'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


def order_successful(request):
    order_number = request.session.get('order_number')
    return render(request, "order_success.html", {'order_number': order_number})

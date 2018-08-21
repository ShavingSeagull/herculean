from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from checkout.forms import MakePaymentForm, OrderForm

# VIEWS TESTS
class CheckoutViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            email='bart@test.com',
            username='bartsimpson',
            password='eatmyshorts2',
            first_name='Bart',
            last_name='Simpson'
        )

        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=45.99,
        )

    def test_checkout_template(self):
        page = self.client.get('/checkout/')

        self.assertTrue(page.status_code, 200)

    def test_checkout_payment_with_valid_credentials(self):
        self.client.login(email='bart@test.com', password='eatmyshorts2')
        product = Product.objects.get(id=1)
        page = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '8',
            'expiry_year': '2025',
            'stripe_id': 'tok_visa',
        })

        self.assertTrue(page.status_code, 200)

    def test_checkout_payment_with_declined_card(self):
        self.client.login(email='bart@test.com', password='eatmyshorts2')
        product = Product.objects.get(id=1)
        page = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '6',
            'expiry_year': '2025',
            'stripe_id': 'tok_chargeDeclined',
        }, follow=True)

        self.assertTemplateNotUsed('order_success.html')


# FORMS TESTS
class CheckoutFormsTests(TestCase):

    def test_valid_payment_form(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '6',
            'expiry_year': '2025',
            'stripe_id': 'xyz555',
        })

        self.assertTrue(form.is_valid())

    def test_payment_form_with_missing_field(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'expiry_month': '10',
            'expiry_year': '2025',
        })

        self.assertFalse(form.is_valid())

    def test_valid_order_form(self):
        form = OrderForm({
            "full_name": "Homer Simpson",
            "house_number": "4321",
            "address1": "Evergreen Terrace",
            "city": "Springfield",
            "county": "Oregon",
            "post_code": "12345",
            "country": "usa",
            "phone_number": "15551234",
        })

        self.assertTrue(form.is_valid())

    def test_order_form_with_missing_field(self):
        form = OrderForm({
            "full_name": "Homer Simpson",
            "house_number": "4321",
            "address1": "Evergreen Terrace",
            "county": "Oregon",
            "post_code": "12345",
            "country": "usa",
            "phone_number": "15551234",
        })

        self.assertFalse(form.is_valid())

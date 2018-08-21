from django.test import TestCase

#VIEWS TESTS
class CartViewsTests(TestCase):

    def test_view_cart_template(self):
        page = self.client.get('/cart/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')

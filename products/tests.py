from django.test import TestCase
from products.models import Product

# VIEWS TESTS
class TestProductsViews(TestCase):

    def setUp(self):
        Product.objects.create(
            name='Test Product',
            slug='test-product',
            description='Test product description',
            price=39.99,
            sku='TESTSKU',
            choice='protein'
        )

    def test_product_list_template(self):
        page = self.client.get('/products/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('products_content.html')

    def test_product_info(self):
        product = Product.objects.get(id=1)
        page = self.client.get('/products/{0}'.format(product.slug))

        self.assertEqual(page.status_code, 200)
        self.assertEqual(product.name, 'Test Product')
        self.assertTemplateUsed('products_item.html')

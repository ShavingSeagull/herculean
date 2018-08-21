from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from reviews.models import Review
from reviews.forms import ReviewForm

# VIEWS TESTS
class TestReviewsViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='maggie@test.com',
            username='maggiesimpson',
            password='IShotMrBurns',
            first_name='Maggie',
            last_name='Simpson',
        )

        Product.objects.create(
            name='Test Product',
            slug='test-product',
            description='Test Description',
            price=45.99,
        )

    def setUp(self):
        user = User.objects.get(id=1)
        product = Product.objects.get(id=1)
        Review.objects.create(
            product=product,
            author=user,
            title='Test Review',
            content='Test review content',
            rating=True
        )

    def test_review_content(self):
        product = Product.objects.get(id=1)
        review = Review.objects.get(id=1)
        page = self.client.get('/products/{0}/reviews/{1}'.format(product.slug, review.id))

        self.assertEqual(page.status_code, 200)
        self.assertEqual(review.title, 'Test Review')
        self.assertTemplateUsed('review_content.html')

    def test_edit_review(self):
        product = Product.objects.get(id=1)
        review = Review.objects.get(id=1)
        page = self.client.get('/products/{0}/reviews/{1}/edit-review'.format(product.slug, review.id))

        self.assertEqual(page.status_code, 302)
        self.assertTemplateUsed('edit_review.html')


# FORMS TESTS
class TestReviewsForms(TestCase):

    def test_add_review_form_valid(self):
        form = ReviewForm({
            'title': 'Test Form',
            'content': 'Test content',
            'rating': True,
        })

        self.assertTrue(form.is_valid())

    def test_add_review_form_invalid(self):
        form = ReviewForm({
            'content': 'Test content',
            'rating': True,
        })

        self.assertFalse(form.is_valid())
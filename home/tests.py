from django.test import TestCase

# VIEWS TESTS
class TestHomeViews(TestCase):

    def test_home_template(self):
        page = self.client.get('/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('index.html')

    def test_about_template(self):
        page = self.client.get('/about')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('about.html')

    def test_delivery_info_template(self):
        page = self.client.get('/delivery-information')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('delivery_info.html')

    def test_club_herculean_template(self):
        page = self.client.get('/club-herculean')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('club_herculean.html')

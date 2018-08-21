from django.test import TestCase
from contact.forms import ContactForm

# VIEWS TESTS
class TestContactViews(TestCase):

    def test_contact_template(self):
        page = self.client.get('/contact/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('contact.html')

    def test_contact_post_method(self):
        page = self.client.post('/contact/', {
            'contact_name': 'Homer Simpson',
            'contact_email': 'homer@test.com',
            'message_subject': 'Test Subject',
            'message_content': 'Test content',
        })

        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/contact/')

# FORMS TESTS
class TestContactForms(TestCase):

    def test_valid_contact_form(self):
        form = ContactForm({
            'contact_name': 'Homer Simpson',
            'contact_email': 'homer@test.com',
            'message_subject': 'Test Subject',
            'message_content': 'Test content',
        })

        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        form = ContactForm({
            'contact_name': 'Homer Simpson',
            'message_subject': 'Test Subject',
            'message_content': 'Test content',
        })

        self.assertFalse(form.is_valid())

from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm

#VIEWS TESTS
class AccountsViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='homer@test.com',
            username='homersimpson',
            password='donuts5',
            first_name='Homer',
            last_name='Simpson'
        )

    def test_login_template(self):
        page = self.client.get('/accounts/login')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')

    def test_login_with_valid_credentials(self):
        page = self.client.post('/accounts/login', {
            'username': 'homersimpson',
            'password': 'donuts5'
        })
        user = User.objects.get(email='homer@test.com')

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)

    def test_register_template(self):
        page = self.client.get('/accounts/register')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')


    def test_edit_profile_template(self):
        page = self.client.get('/accounts/edit-profile')

        self.assertEqual(page.status_code, 302)


# FORMS TESTS
class AccountsFormsTests(TestCase):

    def test_valid_user_registration_form(self):
        form = UserRegistrationForm({
            'username': 'margesimpson',
            'email': 'marge@test.com',
            'password1': 'bluehair3',
            'password2': 'bluehair3'
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_with_existing_username(self):
        form = UserRegistrationForm({
            'username': 'homersimpson',
            'email': 'mrsimpson@test.com',
            'password1': 'donut5',
            'password2': 'donut5',
        })

        self.assertFalse(form.is_valid())

    def test_valid_login_form(self):
        form = UserLoginForm({
            'username_or_email': 'homersimpson',
            'password': 'donuts5',
        })

        self.assertTrue(form.is_valid())

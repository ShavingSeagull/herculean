from django.test import TestCase
from django.contrib.auth.models import User

# VIEWS TESTS
class TestProfilesViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='lisa@test.com',
            username='lisasimpson',
            password='imtoosmart5',
            first_name='Lisa',
            last_name='Simpson'
        )

    def test_profile_template(self):
        user = User.objects.get(id=1)
        page = self.client.get('/profiles/{0}'.format(user.id))

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('profiles.html')

from django.test import TestCase
from django.contrib.auth.models import User
from news.models import Post

# VIEWS TESTS
class TestNewsViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='brian@herculean.com',
            username='brianblessed',
            password='gordansalive1',
            first_name='Brian',
            last_name='Blessed',
            is_staff=True
        )

    def setUp(self):
        user = User.objects.get(id=1)
        Post.objects.create(
            author=user,
            title='Test Post',
            slug='test-post',
            content='Test post content',
            tag='Test'
        )

    def test_news_list_template(self):
        page = self.client.get('/news/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('news_posts.html')

    def test_add_news_post(self):
        self.client.login(email='brian@herculean.com', password='gordansalive1')
        page = self.client.post('/news/add-post')
        post = Post.objects.get(id=1)

        self.assertEqual(page.status_code, 302)
        self.assertEqual(post.title, 'Test Post')

    def test_edit_news_post(self):
        post = Post.objects.get(id=1)
        page = self.client.get('/news/{0}/edit-post'.format(post.slug))

        self.assertEqual(page.status_code, 302)
        self.assertTemplateUsed('edit_post.html')

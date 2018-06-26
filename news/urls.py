from django.conf.urls import url
from .views import get_posts, add_post, edit_post, post_content, delete_post

urlpatterns = [
    url(r'^$', get_posts, name='news'),
    url(r'^add-post$', add_post, name='add-post'),
    url(r'^(?P<slug>[\w-]+)/edit-post$', edit_post, name='edit-post'),
    url(r'^(?P<slug>[\w-]+)/delete-post$', delete_post, name='delete-post'),
    url(r'(?P<slug>[\w-]+)$', post_content, name='post-content'),
]

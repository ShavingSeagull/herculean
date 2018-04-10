from django.conf.urls import url
from .views import get_posts, add_post, post_content

urlpatterns = [
    url(r'^$', get_posts, name='news'),
    url(r'^add-post/$', add_post, name='add-post'),
    url(r'^(?P<pk>\d+)/$', post_content, name='post-content'),
]

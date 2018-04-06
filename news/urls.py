from django.conf.urls import url
from .views import get_posts, add_post

urlpatterns = [
    url(r'^$', get_posts, name='news'),
    url(r'^add-post/$', add_post, name='add-post'),
]

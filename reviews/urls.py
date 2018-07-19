from django.conf.urls import url
from .views import review_content, add_review, edit_review, delete_review


urlpatterns = [
    url(r'^add-review$', add_review, name='add-review'),
    url(r'^(?P<pk>\d+)$', review_content, name='review-content'),
    url(r'^(?P<pk>\d+)/edit-review$', edit_review, name='edit-review'),
    url(r'^(?P<pk>\d+)/delete-review$', delete_review, name='delete-review'),
]

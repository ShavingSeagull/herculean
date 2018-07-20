from django.conf.urls import url
from .views import profile

urlpatterns = [
    url(r'^(?P<pk>\d+)$', profile, name='profiles'),
]

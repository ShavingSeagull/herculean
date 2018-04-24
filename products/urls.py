from django.conf.urls import url
from .views import products

urlpatterns = [
    url(r'^$', products, name='products'),
]

from django.conf.urls import url
from .views import checkout, order_successful

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^order-success$', order_successful, name='order-success'),
]

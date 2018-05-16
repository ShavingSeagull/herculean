from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    url(r'^$', view_cart, name='view-cart'),
    url(r'^add-to-cart/(?P<id>\d+)', add_to_cart, name='add-to-cart'),
    url(r'^adjust/(?P<id>\d+)',adjust_cart, name="adjust-cart"),
]

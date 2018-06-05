from django.conf.urls import url, include
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart
from checkout import urls as checkout_urls

urlpatterns = [
    url(r'^$', view_cart, name='view-cart'),
    url(r'^add-to-cart/(?P<id>\d+)', add_to_cart, name='add-to-cart'),
    url(r'^adjust/(?P<id>\d+)',adjust_cart, name='adjust-cart'),
    url(r'^remove/(?P<id>\d+)', remove_from_cart, name='remove-from-cart'),
    url(r'^checkout/', include(checkout_urls)),
]

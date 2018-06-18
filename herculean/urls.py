from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from home.views import index, about, delivery_info, club_herculean
from contact import urls as contact_urls
from accounts import urls as accounts_urls
from news import urls as news_urls
from products import urls as products_urls
from cart import urls as cart_urls
from .settings import MEDIA_ROOT

urlpatterns = [
    # Admin
    url('admin/', admin.site.urls),
    # Base page
    url(r'^$', index, name="index"),
    url(r'^about/$', about, name='about'),
    url(r'^delivery-information/$', delivery_info, name='delivery-info'),
    url(r'^club-herculean/$', club_herculean, name='club_herculean'),
    # Extended urls
    url(r'^contact/', include(contact_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^news/', include(news_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    # Media
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from home.views import index, about
from contact import urls as contact_urls
from accounts import urls as accounts_urls
from news import urls as news_urls
from products import urls as products_urls
from cart import urls as cart_urls
from .settings import MEDIA_ROOT

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^about/$', about, name='about'),
    url(r'^contact/', include(contact_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^news/', include(news_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

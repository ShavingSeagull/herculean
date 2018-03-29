from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from home.views import index
from accounts import urls as accounts_urls
from news import urls as news_urls
from .settings import MEDIA_ROOT

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^news/', include(news_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

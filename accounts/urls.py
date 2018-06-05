from django.conf.urls import url, include
#from . import urls_reset
from .views import (register, profile, delivery_address, delete_address,
                    edit_profile, edit_address, get_user_posts, delete_user_post,
                    get_current_codes, logout, login)

urlpatterns = [
    url(r'^$', profile, name='accounts_index'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^delivery-address/$', delivery_address, name='delivery-address'),
    url(r'^edit-profile/$', edit_profile, name='edit-profile'),
    url(r'^edit-address/$', edit_address, name='edit-address'),
    url(r'^(?P<pk>\d+)/delete-address/$', delete_address, name='delete-address'),
    url(r'^posts-list/$', get_user_posts, name='posts-list'),
    url(r'^(?P<slug>[\w-]+)/delete-user-post/$', delete_user_post, name='delete-user-post'),
    url(r'^promocodes-list/$', get_current_codes, name='promocodes-list'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    #url(r'^password-reset/', include(urls_reset)),
]

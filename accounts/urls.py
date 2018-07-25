from django.conf.urls import url, include
from . import urls_reset
from .views import (register, profile, edit_profile,
                    get_user_posts, delete_user_post,
                    get_current_codes, logout, login,
                    order_history, order_info)

urlpatterns = [
    url(r'^$', profile, name='accounts_index'),
    url(r'^register$', register, name='register'),
    url(r'^profile$', profile, name='profile'),
    url(r'^edit-profile$', edit_profile, name='edit-profile'),
    url(r'^order-history$', order_history, name='order-history'),
    url(r'^order-history/(?P<pk>\d+)/order-info', order_info, name='order-info'),
    url(r'^posts-list$', get_user_posts, name='posts-list'),
    url(r'^(?P<slug>[\w-]+)/delete-user-post$', delete_user_post, name='delete-user-post'),
    url(r'^promocodes-list$', get_current_codes, name='promocodes-list'),
    url(r'^logout$', logout, name='logout'),
    url(r'^login$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]

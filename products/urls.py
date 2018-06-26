from django.conf.urls import url, include
from .views import products, products_all, product_search, product_item
from reviews import urls as reviews_urls

urlpatterns = [
    url(r'^$', products_all, name='all-products'),
    url(r'^search$', product_search, name='search'),
    url(r'^protein$', products, name='protein'),
    url(r'^creatine$', products, name='creatine'),
    url(r'^amino_acids$', products, name='amino_acids'),
    url(r'^supplements$', products, name='supplements'),
    url(r'^accessories$', products, name='accessories'),
    url(r'^equipment$', products, name='equipment'),
    url(r'^(?P<slug>[\w-]+)$', product_item, name='product-item'),
    url(r'^(?P<slug>[\w-]+)/', include(reviews_urls)),
    #url(r'^reviews/', include(reviews_urls)),
]

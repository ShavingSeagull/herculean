from django.conf.urls import url
from .views import products

urlpatterns = [
    #url(r'^$', products_protein, name='products'),
    url(r'^protein/$', products, name='protein'),
    url(r'^creatine/$', products, name='creatine'),
    url(r'^amino_acids/$', products, name='amino_acids'),
    url(r'^supplements/$', products, name='supplements'),
    url(r'^accessories/$', products, name='accessories'),
    url(r'^equipment/$', products, name='equipment'),
]

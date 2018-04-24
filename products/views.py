from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import resolve
from .models import Product

# def products(request):
#     product_list = Product.objects.all()
#     paginator = Paginator(product_list, 6)
#
#     page = request.GET.get('page')
#     products = paginator.get_page(page)
#     return render(request, "products_content.html", {'products': products})


# def products_protein(request):
#     product_list = Product.objects.filter(choice="protein")
#     paginator = Paginator(product_list, 6)
#
#     page = request.GET.get('page')
#     products = paginator.get_page(page)
#     return render(request, "products_content.html", {'products': products})



def products(request):
    current_url = resolve(request.path_info).url_name
    product_list = Product.objects.filter(choice=current_url)

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products_content.html", {'products': products})

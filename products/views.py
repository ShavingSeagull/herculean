from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from django.urls import resolve
from .models import Product

def products(request):
    """
    Grabs the current url to retrieve the corresponding
    set of products by type (choice) from the database
    and displays them.
    """
    current_url = resolve(request.path_info).url_name
    product_list = Product.objects.filter(choice=current_url)

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products_content.html", {'products': products})


def product_search(request):
    """
    View for searching products by name.
    Didn't create a separate app for this due to
    the fact it only resides within the Products
    section of the site and not on the Nav, as is
    common with other sites.
    """
    product_list = Product.objects.filter(name__icontains=request.GET['q']).order_by('name')

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products_content.html", {'products': products})

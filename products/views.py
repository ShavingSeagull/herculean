from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

def products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products_content.html", {'products': products})

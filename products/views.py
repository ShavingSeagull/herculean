from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import resolve
from django.utils import timezone
from .models import Product
from reviews.models import Review

def products(request):
    """
    Grabs the current url to retrieve the corresponding
    set of products by type (choice) from the database
    and displays them.
    """
    current_url = resolve(request.path_info).url_name
    product_list = Product.objects.filter(choice=current_url).order_by('name')

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products_content.html", {'products': products})


def products_all(request):
    """
    Exists to show all products if someone enters
    'products/' into the address bar. There is no link
    for this on the site, but this view will circumvent
    any hard input from curious users.
    """
    product_list = Product.objects.all().order_by('name')

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


def product_item(request, slug):
    """
    Manages the in-depth view of an individual product.
    """
    product = get_object_or_404(Product, slug=slug)
    product.save()

    ratings = Review.objects.filter(product=product)
    pos_total = 0
    neg_total = 0

    for score in ratings:
        if score.rating == True:
            pos_total += 1
        else:
            neg_total += 1

    review_list = Review.objects.filter(product=product, created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(review_list, 3)

    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    return render(request, "product_item.html", {"product": product, "pos_ratings": pos_total,
                                                 "neg_ratings": neg_total, "reviews": reviews})


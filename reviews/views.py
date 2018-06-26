from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from products.models import Product
#from products.views import product_item
from .models import Review
from .forms import ReviewForm

def get_reviews(request):
    """
    View that displays list of reviews in
    date order from newest to oldest.
    """
    review_list = Review.objects.filter(created_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(review_list, 5)

    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    return render(request, "reviews.html", {'reviews': reviews})


def review_content(request, pk):
    """
    Function for showing the individual review in full
    """
    review = get_object_or_404(Review, pk=pk)
    review.save()
    return render(request, "review_content.html", {'review': review})


# @login_required
# def add_review(request):
#     """
#     View for adding reviews via use of the ReviewForm.
#     Utilises checks to ensure that only members can post
#     reviews.
#     """
#     if request.user:
#         if request.method == "POST":
#             review_form = ReviewForm(request.POST)
#             if review_form.is_valid():
#                 review = review_form.save(commit=False)
#                 #review.product = request.product
#                 review.author = request.user
#                 review_form.save()
#
#                 messages.success(request, "Review posted successfully!")
#                 return redirect(reverse('product-item'))
#         else:
#             review_form = ReviewForm()
#     else:
#         messages.error(request, "You must be a member to post reviews.")
#         return redirect(reverse('get_reviews'))
#
#     args = {'review_form': review_form}
#     return render(request, "add_review.html", args)


@login_required
def add_review(request, slug):
    """
    View for adding reviews via use of the ReviewForm.
    Utilises checks to ensure that only members can post
    reviews.
    """
    if request.user:
        product = get_object_or_404(Product, slug=slug) if slug else None
        if request.method == "POST":
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.author = request.user
                review_form.save()

                messages.success(request, "Review posted successfully!")
                return redirect(reverse('product-item'))
        else:
            review_form = ReviewForm()
    else:
        messages.error(request, "You must be a member to post reviews.")
        return redirect(reverse('product-item'))

    args = {'review_form': review_form}
    return render(request, "add_review.html", args)


@login_required
def edit_review(request, pk=None):
    """
    Function for editing a review.
    Renders the form with the current content for clarification.
    """
    if request.user:
        review = get_object_or_404(Review, pk=pk) if pk else None
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review_form.save()
                return redirect(review_content, review.pk)
        else:
            review_form = ReviewForm(instance=review)
        return render(request, "edit_review.html", {'review_form': review_form})
    else:
        messages.error(request, "You have to be a member to edit reviews.")
        return redirect(reverse(get_reviews))


@login_required
def delete_review(request, pk=None):
    """
    Function for deleting individual reviews.
    """
    if request.user:
        review = get_object_or_404(Review, pk=pk) if pk else None
        review.delete()

        messages.success(request, "Review deleted successfully.")
        return redirect(reverse(get_reviews))
    else:
        messages.error(request, "Only members can delete posts.")
        return redirect(reverse(get_reviews))

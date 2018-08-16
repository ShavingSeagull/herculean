from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from herculean.urls import index
from .models import Review
from .forms import ReviewForm

def review_content(request, slug, pk):
    """
    Function for showing the individual review in full
    """
    product = get_object_or_404(Product, slug=slug)
    review = get_object_or_404(Review, pk=pk)
    review.save()
    return render(request, "review_content.html", {'review': review})


@login_required
def add_review(request, slug, pk=None):
    """
    View for adding reviews via use of the ReviewForm.
    Utilises checks to ensure that only members can post
    reviews.
    """
    if request.user:
        product = get_object_or_404(Product, slug=slug)
        if request.method == "POST":
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.author = request.user
                review_form.save()

                return redirect('/products/' + slug)
        else:
            review_form = ReviewForm()
    else:
        messages.error(request, "You must be a member to post reviews.")
        return redirect('/products/' + slug)

    args = {'review_form': review_form, 'slug': slug}
    return render(request, "add_review.html", args)


@login_required
def edit_review(request, slug, pk=None):
    """
    Function for editing a review.
    Renders the form with the current content for clarification.
    """
    if request.user:
        product = get_object_or_404(Product, slug=slug)
        review = get_object_or_404(Review, pk=pk) if pk else None
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review_form.save()
                return redirect('/products/' + slug)
        else:
            review_form = ReviewForm(instance=review)
        return render(request, "edit_review.html", {'review_form': review_form})
    else:
        return redirect(reverse(index))


@login_required
def delete_review(request, slug, pk=None):
    """
    Function for deleting individual reviews.
    """
    if request.user:
        product = get_object_or_404(Product, slug=slug)
        review = get_object_or_404(Review, pk=pk) if pk else None
        review.delete()

        return redirect('/products/' + slug)
    else:
        return redirect(reverse(index))

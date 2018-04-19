from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """
    Gets a list of all post items and renders them in
    descending order - most recent to oldest.
    Paginator limits them to 7 per page.
    """
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(post_list, 7)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "news_posts.html", {'posts': posts})


def post_content(request, slug):
    """
    Function for showing the individual news item in full
    """
    post = get_object_or_404(Post, slug=slug)
    #post.views += 1
    post.save()
    return render(request, "post_content.html", {'post': post})


@login_required
def add_post(request):
    """
    Function for adding posts via use of the BlogPostForm.
    Utilises checks to ensure that only staff members can post
    news items
    """
    if request.user.is_staff:
        if request.method == "POST":
            post_form = BlogPostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.author = request.user
                post_form.save()
                messages.success(request, "News item posted successfully!")
                return redirect(reverse(get_posts))
        else:
            post_form = BlogPostForm()
    else:
        messages.error(request, "You must be a staff member to post a news item.")
        return redirect(reverse(get_posts))

    args = {'post_form': post_form}
    return render(request, "add_post.html", args)


@login_required
def edit_post(request, slug=None):
    """
    Function for editing a post.
    Renders the form with the current content for clarification.
    """
    if request.user.is_staff:
        post = get_object_or_404(Post, slug=slug) if slug else None
        if request.method == 'POST':
            post_form = BlogPostForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.author = request.user
                post_form.save()
                return redirect(post_content, post.slug)
        else:
            post_form = BlogPostForm(instance=post)
        return render(request, "edit_post.html", {'post_form': post_form})
    else:
        messages.error(request, "You have to be a member of staff to edit posts.")
        return redirect(reverse(get_posts))

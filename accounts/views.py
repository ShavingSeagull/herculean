from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import UserLoginForm, UserRegistrationForm, UserForm, ProfileForm
from .models import Profile
from news.models import Post
from promocodes.models import PromoCode


def index(request):
    """Displays the index page"""
    return render(request, "index.html")


def logout(request):
    """Logs the user out and redirects them back to the index page"""
    auth.logout(request)
    return redirect(reverse('index'))


def login(request):
    """Handles the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user and user.is_active:  # Passes the rejection message if user has had 'is_active' flag set to false
                auth.login(request, user)

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    """Handles the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered!")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "Unable to log you in at this time. Please refresh and try again.")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required
def profile(request):
    """Displays the profile page of a user who is logged-in"""
    return render(request, 'profile_content.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile was successfully updated!")
            return redirect(reverse('profile'))
        else:
            messages.error(request, "Update unsuccessful. Please rectify the problem below")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    args = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'edit_profile.html', args)


@login_required
def get_user_posts(request):
    """
    Retrieves all post items created by the authenticated user
    and lists them 4 to a page using Paginator, from newest to oldest
    """
    if request.user.is_staff:
        post_list = Post.objects.filter(author=request.user, published_date__lte=timezone.now()).order_by('-published_date')
        paginator = Paginator(post_list, 4)

        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, "post_list.html", {'posts': posts})
    else:
        messages.error(request, "That section is only available for staff.")
        return redirect(reverse(profile))


@login_required
def delete_user_post(request, slug=None):
    """
    Deletes an individual post. Similar to delete view in News app,
    but this redirects to the profile page as the action is conducted
    from there initially.
    """
    if request.user.is_staff:
        post = get_object_or_404(Post, slug=slug) if slug else None
        post.delete()

        messages.success(request, "Post deleted successfully.")
        return redirect(reverse(get_user_posts))
    else:
        messages.error(request, "Only staff can delete posts.")
        return redirect(reverse(profile))


@login_required
def get_current_codes(request):
    """
    Verifies user is logged in and retrieves all the current discount
    codes that are active (Active=True and within the dates provided).
    """
    if request.user:
        promo_list = PromoCode.objects.filter(start_date__lte=timezone.now(), expiry_date__gte=timezone.now(), active=True).order_by('name')
        paginator = Paginator(promo_list, 6)

        page = request.GET.get('page')
        codes = paginator.get_page(page)
        return render(request, "promo_list.html", {'codes': codes})
    else:
        messages.error(request, "You have to be a member to see that.")
        return redirect(reverse(profile))

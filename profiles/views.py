from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def profile(request, pk):
    """
    Retrieves the User by pk and renders the info for display
    """
    # Can't call the variable 'user' because it causes clashes with the actual user
    # object when used on other templates
    user_info = get_object_or_404(User, pk=pk)
    user_info.save()
    return render(request, "profiles.html", {'user_info': user_info})

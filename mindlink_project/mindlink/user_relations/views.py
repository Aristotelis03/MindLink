from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from user_relations.models import Relations
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required  # Import login_required decorator

@login_required(login_url='/login')
def toggle_follow(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    # Check if the current user is already following the target user
    is_following = Relations.objects.filter(follower=target_user, following=request.user).exists()

    if is_following:
        # If already following, unfollow
        Relations.objects.filter(follower=target_user, following=request.user).delete()
    else:
        # If not following, follow
        Relations.objects.create(follower=target_user, following=request.user)

    user_profile_url = reverse('user_profile_view', args=[target_user.username])
    return redirect(user_profile_url)


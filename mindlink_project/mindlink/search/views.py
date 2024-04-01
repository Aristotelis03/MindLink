from re import search
from hashtags.models import Hashtag
from accounts.models import CustomUser
from post.models import Post
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required  # Import login_required decorator

@login_required(login_url='/login')
def users_results_view(request, search_input):
    users_results = CustomUser.objects.filter(username__icontains=search_input)
    hashtags_results = Hashtag.objects.filter(name__icontains=search_input)
    posts_results = Post.objects.filter(content__icontains=search_input)
    context = {
        'search_input' : search_input,
        'users_results' : users_results,
        'hashtags_results' : hashtags_results,
        'posts' : posts_results,
    }

    
    if not users_results:
        context['no_users_found'] = True

    
    if not hashtags_results:
        context['no_hashtag_found'] = True
    
    if not posts_results:
        context['no_posts_found'] = True 

    return render(request, 'search.html', context)




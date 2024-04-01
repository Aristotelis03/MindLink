from multiprocessing import current_process
from os import name
from django.shortcuts import get_object_or_404, render
from hashtags.models import Hashtag
from post.models import Post
from django.contrib.auth.decorators import login_required  # Import login_required decorator

@login_required(login_url='/login')
# Create your views here.
# def trending_hashtags_view(request):
#     trending_hashtags = Hashtag.objects.all()  # Adjust this based on your criteria for "trending"
#     return render(request, 'trending_hashtags.html', {'trending_hashtags': trending_hashtags})

def hashtag_posts_view(request, hashtag):
    current_hashtag = get_object_or_404(Hashtag, name=hashtag)
    posts = current_hashtag.post.all() # type: ignore
    context = {
        'hashtag': current_hashtag,
        'posts': posts,
    }
    return render(request, 'hashtag_posts.html',context)
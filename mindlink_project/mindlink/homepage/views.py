from django.shortcuts import redirect, render,get_object_or_404
from post.models import Post, Like, Comments
from post.forms import CreateCommentForm
from django.contrib.auth.decorators import login_required  # Import login_required decorator

@login_required(login_url='/login')
def home(request):    
    message = "You have to log in"
    comment_form = CreateCommentForm()


    # pass logged in users name in side bar
    message = request.user
    # Short the post by creation time
    posts = Post.objects.all().order_by('-created_at')
    print(request.user.username)

    # Retrieve comments for each post and add them to the post instance
    for post in posts:
        post.comments = Comments.objects.filter(post=post)

    return render(request, "home.html", {'message': message, 'posts': posts, 'comment_form': comment_form})

@login_required(login_url='/login')
def sidebar_view(request):
    return render(request,"sidebar.html")


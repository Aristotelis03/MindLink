from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import CustomUser
from post.forms import CreateCommentForm, Post, Comments
from user_relations.models import Relations
from django.contrib.auth.decorators import login_required  # Import login_required decorator

# Create your views here.
@login_required(login_url='/login')
def user_profile_view(request, user):
    user_p = get_object_or_404(CustomUser, username=user)
    comment_form = CreateCommentForm()

    # Load Posts
    posts = Post.objects.filter(user=user_p.id).order_by('-created_at')
    # Load Follow
    follow_tags = Relations.objects.filter(follower=request.user, following=user_p)

    if request.method == 'POST':
        comment_form = CreateCommentForm(request.POST)
        
        if comment_form.is_valid():
            post_id = comment_form.cleaned_data.get('post_id')
            post = Post.objects.get(pk=post_id)
            comment = comment_form.save(commit=False)
            comment.user = user_p.id
            comment.post = post
            print("Comment saved:", comment)  
            return redirect('/user_profile')   
        else:
            print("form is not valid")
            for field, errors in comment_form.errors.items():
                for error in errors:
                    print(f"Field: {field}, Error: {error}")
    else:
        comment_form = CreateCommentForm()

    # pass logged in users name in side bar
    message = request.user

    print(user_p.username)

    # Retrieve comments for each post and add them to the post instance
    for post in posts:
        post.comments = Comments.objects.filter(post=post)  
        
    context = {'posts': posts, 'user_p': user_p, 'comment_form': comment_form, 'follow_tags': follow_tags, 'message': message}
    return render(request, 'user_profile.html',context)

@login_required(login_url='/login')
def favorites_view(request):

    user = get_object_or_404(CustomUser, pk=request.user.id)
    posts = user.favorites_post.all()
    context = {'posts': posts}
    return render(request, 'display_favorites.html',context)
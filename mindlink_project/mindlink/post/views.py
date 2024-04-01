from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from post.models import Like, Post,Comments , Favorites
from .forms import CreateCommentForm, CreatePostForm
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize

# Create your views here.
@login_required(login_url='/login/')
def test(request):
    return render(request, "test.html")

@login_required(login_url='/login/')
def create_post_view(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/home')
    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required(login_url='/login/')
def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user or request.user.id == 1 :
        post.delete()
        # messages.success(request, 'Post deleted successfully.')

    return redirect('/home')  # Redirect to an appropriate view after deletion

@login_required(login_url='/login/')
def create_comments_view(request):
    if request.method == 'POST':
        comment_form = CreateCommentForm(request.POST)
        
        if comment_form.is_valid():
            post_id = comment_form.cleaned_data.get('post_id')
            post = get_object_or_404(Post, pk=post_id)
            
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            # print("Comment saved:", comment)  
            return JsonResponse({'success' : True})

        else:
            return JsonResponse({'success': False, 'errors': comment_form.errors})
    else:
        comment_form = CreateCommentForm()
        # return HttpResponse('Comment submitted successfully')
        # return render(request, 'create_comments.html', {'comment_form' : comment_form})
        return JsonResponse({'comment_form' : comment_form})

# like posts


# def like_post_view(request,post_id):
#     post = get_object_or_404(Post, pk=post_id)

#     # Check if the like already exists
#     if post.likes.filter(id=request.user.id).exists():
#         # User has already liked the post, so unlike it
#         post.likes.remove(request.user)
#         print("Like removed.")
#     else:
#         # User hasn't liked the post, so like it
#         post.likes.add(request.user)
#         print("Like added.")
           
#     return redirect('/home')

@login_required(login_url='/login/')
def like_post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        message = "Like removed."

    else:
        post.likes.add(request.user)
        message = "Like added."

    likes_count = post.likes.count()
    
    like_instance = Like(user=request.user, post=post)
    print(like_instance)

    response_data = {
        'message': message,
        'likes_count': likes_count,
    }
    print(message)
    return JsonResponse(response_data)
# Comments

@login_required(login_url='/login/')
def like_comment_view(request,comment_id):
    comment = get_object_or_404(Comments, pk=comment_id)
    
    # Check if the like already exists
    if comment.likes.filter(id=request.user.id).exists():
        # User has already liked the post, so unlike it
        comment.likes.remove(request.user)
        message = "Like removed."
    else:
        # User hasn't liked the post, so like it
        comment.likes.add(request.user)
        message = "Like added."
        
    likes_count = comment.likes.count()
    # like_instance = Like(user=request.user, comment=comment)
    # print(like_instance)

    response_data = {
        'message': message,
        'likes_count': likes_count,
    }
    return JsonResponse(response_data)

# def delete_comment_view(request,comment_id):
#     comment = Comments.objects.filter(id= comment_id)
#     session_id = request.session.get('id')

#     # Make it more secure !!!
#     comment.filter().delete()
#     return redirect('/home')

@login_required(login_url='/login/')
def delete_comment_view(request,comment_id):
    comment = get_object_or_404(Comments, id=comment_id)           
    # Check if the user has permission to delete the comment
    if request.user == comment.user:
        comment.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Permission denied'})

@login_required(login_url='/login/')
def toggle_favorite(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Toggle favorite status
    if request.user in post.favorited_by.all():
        request.user.favorites_post.remove(post)
        message = "Removed From Favorites."
    else:
        request.user.favorites_post.add(post)
        message = "Added To Favorites."
        
    favorites_instance = Favorites(user=request.user, post=post)
    print(favorites_instance)
    response_data = {
        'message': message,

    }
    print(message)
    return JsonResponse(response_data)

# views.py

# def get_comments(request, post_id):
#     comments = Comments.objects.filter(post_id = post_id)
#     posts = Post.objects.all().order_by('-created_at')

#     for post in posts:
#         post.comments = Comments.objects.filter(post=post)
#     # serialized_comments = serialize('json', comments)
#     return render(request, 'display_comments.html', {'posts': posts})

@login_required(login_url='/login/')
def get_comments(request, post_id):
    # Your logic to fetch comments for the given post_id
    comments = Comments.objects.filter(post_id=post_id)
    print(comments)
    return render(request, 'comments.html', {'comments': comments})

from django.contrib import admin
from django.urls import path,include

# importing views from views..py
from .views import test, create_comments_view,create_post_view, like_post_view, like_comment_view, delete_comment_view, toggle_favorite,get_comments,delete_post_view

urlpatterns = [
    path('test/', test),
    # path('display_posts/', display_posts_view),
    path('create_comments/', create_comments_view, name='create_comments'),
    path('delete_post/<int:post_id>/', delete_post_view, name='delete_post'),
    path('get_comments/<int:post_id>/', get_comments, name='get_comments'),
    path('create_post/', create_post_view, name='create_post_view'),
    path('like_post/<int:post_id>/', like_post_view, name='like_post_view'),
    path('like_comment/<int:comment_id>/', like_comment_view, name='like_comment_view'),
    path('delete_comment/<int:comment_id>/', delete_comment_view, name='delete_comment_view'),
    path('toggle_favorite/<int:post_id>/', toggle_favorite, name='toggle_favorite'),

]

from django.contrib import admin
from django.urls import path,include

# importing views from views..py
from .views import hashtag_posts_view
urlpatterns = [
    path('hashtag_posts/<slug:hashtag>/', hashtag_posts_view, name='hashtag_posts'),
    # path('trending_hashtags/', trending_hashtags_view, name='trending_hashtags_view'),
]

from django.contrib import admin
from django.urls import path,include

# importing views from views..py
from .views import users_results_view
urlpatterns = [
    path('search/<slug:search_input>/', users_results_view, name='users_results'),
    # path('trending_hashtags/', trending_hashtags_view, name='trending_hashtags_view'),
]

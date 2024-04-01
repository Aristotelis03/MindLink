from django.urls import path

# importing views from views..py
from .views import user_profile_view,favorites_view

urlpatterns = [
    path('user_profile/<slug:user>/', user_profile_view, name='user_profile_view'),
    path('favorites/', favorites_view, name='favorites_view')

]
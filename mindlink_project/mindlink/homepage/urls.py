from django.contrib import admin
from django.urls import path,include

# importing views from views..py
from .views import home ,sidebar_view
urlpatterns = [
    path('home/', home, name='home'),
    path('sidebar/', sidebar_view),
]

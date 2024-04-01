from django.contrib import admin 
from django.urls import include, path 

  
# importing views from views..py 
from .views import login_view, register_view, logout_view, recover 
  
urlpatterns = [ 
    path('login/', login_view), 
    path('register/', register_view, name='register'), 
    path('recover/', recover), 
    path('logout/', logout_view), 
] 
from django.urls import path
from .views import toggle_follow

urlpatterns = [
    # ... other URLs ...
    path('toggle_follow/<int:user_id>/', toggle_follow, name='toggle_follow'),
    # path('friends/', friends_view, name = 'friends'),
]
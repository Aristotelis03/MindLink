from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Custom user model that inherits from built in Users
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True, default='pictures/default_profile_picture/profile_picture.png')    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    followers = models.ManyToManyField('self',  through='user_relations.Relations', symmetrical=False, related_name='following_users')
    favorites_post = models.ManyToManyField('post.Post', related_name='favorited_by')


    # Use unique related_name values to avoid clashes
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_permissions')


    def __str__(self):
        return self.username    
    
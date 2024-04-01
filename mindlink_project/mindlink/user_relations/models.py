from accounts.models import CustomUser
from django.db import models

# Create your models here.
class Relations(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='followers_relations', on_delete=models.CASCADE, null=True)
    following = models.ForeignKey(CustomUser, related_name='following_relations', on_delete=models.CASCADE, null=True)

 
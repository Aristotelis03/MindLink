from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser
from hashtags.models import Hashtag

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts')
    favorites_user = models.ManyToManyField(CustomUser, through= 'Favorites', related_name='favorite_posts')
    hashtags = models.ManyToManyField(Hashtag, related_name='post')

    def __str__(self):
        return self.user.username + " post " + str(self.pk) + " - " + str(self.created_at)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Extract hashtags from the post content
        hashtags_list = self.extract_hashtags()

        # Associate the hashtags with the post
        self.associate_hashtags(hashtags_list)

    def extract_hashtags(self):

        # Here's a simple example using regular expressions:
        import re
        content = self.content
        hashtags_list = re.findall(r'#\w+', content)
        return hashtags_list

    def associate_hashtags(self, hashtags_list):
        # Associate the extracted hashtags with the post
        for hashtag_name in hashtags_list:
            hashtag, created = Hashtag.objects.get_or_create(name=hashtag_name[1:])  # Removing the '#' character
            self.hashtags.add(hashtag)    

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} to {self.post}'

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_comments')

    def __str__(self):
        return f'{self.user.username} on {self.post}'

class Favorites(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta: 
        unique_together = ('user','post')

    def __str__(self):
        return f'{self.user.username} to {self.post.pk}'

class Test(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    


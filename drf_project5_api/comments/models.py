from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    '''
    Comment will link with the user wo created and the post
    that was commented on
    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s comment"

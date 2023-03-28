from django.db import models
from posts.models import Post
from django.contrib.auth.models import User


class Like(models.Model):
    '''
    Like class for liking a post, this will allow user to keep
    track of there liked posts
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # this is to make sure the post cant be liked again by the same user
        unique_together = ['owner', 'post']
    
    def __str__(self):
        return f'{self.owner} and {self.post}'
from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    '''
    Like class for liking a post, this will allow user to keep
    track of there liked posts
    '''
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # this is to make sure the post cant be liked again by the same user
        unique_together = ['owner', 'followed']
    
    def __str__(self):
        return f'{self.owner} is following {self.followed}'

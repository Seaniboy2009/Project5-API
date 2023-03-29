from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class VoteAlike(models.Model):
    '''
    Vote like class
    this class is for a user to confirm they think the advert and 
    given product are alike
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='alike', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # this is to make sure the post cant be liked again by the same user
        unique_together = ['owner', 'post']
    
    def __str__(self):
        return f'{self.owner} thinks {self.post} is alike'


class VoteNotAlike(models.Model):
    '''
    Vote like class
    this class is for a user to confirm they think the advert and 
    given product are alike
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='notalike', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # this is to make sure the post cant be liked again by the same user
        unique_together = ['owner', 'post']
    
    def __str__(self):
        return f'{self.owner} thinks {self.post} is not alike'
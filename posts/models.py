from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    '''
    Post will have the comparison images as well as the vote buttons
    '''

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    advert_image = models.ImageField(
        upload_to='images/',
        default='../media/images/default_post_keitpn',
    )
    reality_image = models.ImageField(
        upload_to='images/',
        default='../media/images/default_post_keitpn',
    )
    location = models.CharField(max_length=255, blank=True)
    franchisor = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Post:{self.id},Owner:{self.owner}, Post:{self.id}"




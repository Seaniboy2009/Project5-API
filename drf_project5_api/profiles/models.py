from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(
        upload_to='Project 5 API/',
        default='../default_profile_o21i6o_tvkkll',
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Profile belongs to {self.owner}"
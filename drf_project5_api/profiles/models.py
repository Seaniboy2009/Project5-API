from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    '''
    Profile has a one to one field to the owners user account and is created
    once a new user is created
    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../media/images/default_profile_o21i6o_h3tqjf',
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

# Each time a user is created this will call the create profile function
post_save.connect(create_profile, sender=User)
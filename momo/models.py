from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    """relationship between User (the one which is built in django) and the one you are creating"""
    user = models.OneToOneField(User,on_delete= models.CASCADE)

    #additional attributes
    picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

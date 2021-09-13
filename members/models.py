from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=CASCADE, related_name="profile")
    bio = models.CharField(max_length=255)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(null=True, blank=True, max_length=255)
    facebook_url = models.CharField(null=True, blank=True, max_length=255)
    twitter_url = models.CharField(null=True, blank=True, max_length=255)
    instagram_url = models.CharField(null=True, blank=True, max_length=255)



    def __str__(self):
        return str(self.user)

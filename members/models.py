from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)

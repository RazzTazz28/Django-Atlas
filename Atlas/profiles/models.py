from django.db import models
from django.conf import settings
from accounts.models import NewUser


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    avatar = models.ImageField(default='Untitled.png', upload_to='profileIMG/')

    def __str__(self):
        return self.user

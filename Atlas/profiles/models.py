from django.db import models
from django.conf import settings
from accounts.models import NewUser


class UserProfile(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, related_name='profile')

    avatar = models.ImageField(default='Untitled.png', upload_to='profileIMG/')

    def __str__(self):
        return str(self.user)

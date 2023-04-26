from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_img = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

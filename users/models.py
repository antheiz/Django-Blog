from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_img = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.profile_img.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            img.save(
                self.profile_img.path
            )  # Save it again and override the larger image

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return (f"{self.user.username} profile")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        imag = Image.open(self.image.path)

        if imag.height > 300 or imag.width > 300:
            out_size = (300, 300)
            imag.thumbnail(out_size)
            imag.save(self.image.path)

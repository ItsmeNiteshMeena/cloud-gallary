from django.db import models

# Create your models here.

from cloudinary.models import CloudinaryField
class PhotoAsset(models.Model):
    title = models.CharField(max_length=255)
    caption= models.TextField(blank=True)
    category=models.CharField(max_length=100)
    image=CloudinaryField('image')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models
from distutils.command.upload import upload

# Create your models here.


class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')

from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/',default="Admin.png")
    Bio = models.TextField()

    
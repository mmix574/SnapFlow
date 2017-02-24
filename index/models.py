from django.db import models

# Create your models here.


# class User (models.Model):
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    lang = models.CharField(max_length=10)
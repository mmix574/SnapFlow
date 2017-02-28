from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User)
    tittle = models.CharField(max_length=20)
    content = models.CharField(max_length=120)
    created_time = models.DateTimeField(auto_now=True)
    last_operate = models.DateTimeField(auto_now_add=True)

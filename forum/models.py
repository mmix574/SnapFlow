from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    name = models.CharField(max_length=20)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now=True,blank=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name


# Create your models here.
class Thread (models.Model):
    tittle = models.CharField(max_length=20,blank=True)
    content = models.TextField(default="")
    create_user = models.ForeignKey(User,default=1)
    create_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

class TAG(models.Model):
    pass
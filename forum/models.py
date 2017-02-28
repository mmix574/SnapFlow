from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread (models.Model):
    name = models.CharField(max_length=10)


class Class(models.Model):
    name = models.CharField(max_length=20)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now=True)
    last_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SubClass(models.Model):
    name = models.CharField(max_length=20)
    pclass = models.ForeignKey(Class)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now=True)
    last_time = models.DateTimeField(auto_now_add=True)

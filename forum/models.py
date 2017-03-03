from django.db import models
from django.contrib.auth.models import User




class Class(models.Model):
    name = models.CharField(max_length=20)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now=True)
    last_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
class Thread (models.Model):
    name = models.CharField(max_length=10)



class TAG(models.Model):
    pass
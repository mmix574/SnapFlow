from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from forum.models import Thread


class Collection(models.Model):
    thread = models.ForeignKey(Thread)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True)
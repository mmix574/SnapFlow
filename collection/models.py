from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from forum.models import Thread


class Collection(models.Model):
    thread = models.ForeignKey(Thread)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "问题收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.create_user.username +" 收藏的"+self.thread.tittle[:20]+"..."


from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class AdminBroadCast(models.Model):
    create_user = models.ForeignKey(User)
    tittle = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    sended = models.BooleanField(default=0)

    def __str__(self):
        return self.tittle

    #
    class Meta:
        verbose_name = "管理广播"
        verbose_name_plural = verbose_name
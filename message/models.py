from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserToUserMessage(models.Model):
    pass


class SystemToUserMessage(models.Model):
    user = models.ForeignKey(User,default=1)
    content = models.CharField(max_length=500,null=True,blank=True)
    read = models.BooleanField(default=False)
    time = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "系统消息"
        verbose_name_plural = verbose_name
        pass
    pass

# @ 回复等，点赞等
class EventMessage(models.Model):
    pass



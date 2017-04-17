from django.db import models
from django.contrib.auth.models import User


# Create your models here.


from django.contrib.auth.models import User

class UserMessageStatus(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    user_to_user_message_count = models.IntegerField(default=0)
    system_to_user_message_count = models.IntegerField(default=0)
    even_message_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "用户信息状态"
        verbose_name_plural = verbose_name

class UserToUserMessage(models.Model):

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class SystemToUserMessage(models.Model):
    user = models.ForeignKey(User)
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

    class Meta:
        verbose_name = "事件消息"
        verbose_name_plural = verbose_name


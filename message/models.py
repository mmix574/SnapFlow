from django.db import models
from django.contrib.auth.models import User


# Create your models here.


from django.contrib.auth.models import User

class MessageStatus(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User)
    user_to_user_message_count = models.IntegerField(default=0)
    system_to_user_message_count = models.IntegerField(default=0)
    even_message_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "用户信息状态"
        verbose_name_plural = verbose_name

class UserToUserMessage(models.Model):
    user = models.ForeignKey(User,related_name="A_user")
    to_user = models.ForeignKey(User,related_name="B_user")
    content = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "私信"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class SystemToUserMessage(models.Model):
    user = models.ForeignKey(User)
    tittle = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content+"->"+self.user.username
    class Meta:
        verbose_name = "系统消息"
        verbose_name_plural = verbose_name
        pass




# @ 回复等，点赞等
class EventMessage(models.Model):

    class Meta:
        verbose_name = "事件消息"
        verbose_name_plural = verbose_name



class Friend(models.Model):
    user = models.ForeignKey(User)
    has_friend = models.ForeignKey(User,related_name="myfriend")
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "朋友"
        verbose_name_plural = verbose_name


pass

from django.db.models.signals import post_save


def create_message_status(sender,instance,created,**kwargs):
    if created:
        ms = MessageStatus()
        ms.user = instance
        ms.save()

post_save.connect(create_message_status,User)



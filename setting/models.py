from django.db import models

# Create your models here.


class SystemEmailInfo(models.Model):
    email_address = models.CharField(max_length=255)
    name = models.CharField(default="admin",max_length=20)
    port = models.IntegerField()
    protocal = models.CharField(max_length=20)

    class Meta:
        verbose_name = "系统邮箱"
        verbose_name_plural = verbose_name


class WelcomeSystemMessage(models.Model):
    tittle = models.CharField(max_length=80)
    content = models.TextField(default="",blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "初始化系统消息"
        verbose_name_plural = verbose_name


# events

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from message.services import send_system_message_to_single_user
@receiver(post_save,sender=User)
def send_system_message(sender,instance,created,**kwargs):
    if created:
        wsm = WelcomeSystemMessage.objects.all()
        for m in wsm:
            send_system_message_to_single_user(instance,m.tittle,m.content)



# 2017年4月19日23:36:42
# UserCredit 奖励情况表

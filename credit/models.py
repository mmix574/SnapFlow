from django.db import models

from django.contrib.auth.models import User

class CreditDefault(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    credit_point = models.IntegerField(default=0)
    last_modify = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "用户积分"
        verbose_name_plural = verbose_name

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_credit_information(sender,instance,created,**kwargs):
    if created:
        ucd = CreditDefault()
        ucd.user = instance
        ucd.save()

class CashPoint(models.Model):
    pass

    class Meta:
        verbose_name = "现金积分"
        verbose_name_plural = verbose_name


class UserCreditNickName(models.Model):
    name = models.CharField(max_length=10)
    start_point = models.IntegerField()
    end_point = models.IntegerField()

    general_level = models.IntegerField(default=0)
    # 最大最小
    index = models.IntegerField()


    class Meta:
        verbose_name = "用户积分称号"
        verbose_name_plural = verbose_name



class EveryDayCreditLog(models.Model):
    pass

class ThreadViewLog(models.Model):
    pass


class OnlineLog(models.Model):
    pass

class CreditExchangeCode(models.Model):
    code = models.CharField(max_length=32)
    point = models.IntegerField(default=0)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "积分兑换"
        verbose_name_plural = verbose_name


# 积分事件绑定
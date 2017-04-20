from django.db import models

from django.contrib.auth.models import User

class CreditStatus(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    credit_point = models.IntegerField(default=0)
    last_modify = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "用户积分状态"
        verbose_name_plural = verbose_name

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# 自动生成CreditDefault
@receiver(post_save,sender=User)
def create_credit_information(sender,instance,created,**kwargs):
    if created:
        ucd = CreditStatus()
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



from forum.models import Thread
class ThreadViewLog(models.Model):
    thread = models.ForeignKey(Thread)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)


class OnlineLogManager(models.Manager):
    def today(self):
        from django.utils import timezone
        from django.utils.timezone import datetime,timedelta

        today = timezone.now().date()
        tomorrow = today + timedelta(1)

        today = timezone.make_aware(today, timezone.get_current_timezone())
        tomorrow = timezone.make_aware(tomorrow, timezone.get_current_timezone())

        return self.filter(time__lte=tomorrow, time__gte=today)

class OnlineLog(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)

    objects= OnlineLogManager()

    class Meta:
        verbose_name = "在线记录"
        verbose_name_plural = verbose_name


class EverydaySign(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

class CreditExchangeCode(models.Model):
    code = models.CharField(max_length=32)
    point = models.IntegerField(default=0)
    used = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "积分兑换"
        verbose_name_plural = verbose_name


class CreditLog(models.Model):
    choices_types = (('answering','回答'),('asking','提问'),('everyday_login','每日登陆'),('everyday_sign','每日签到'),('online_reward','在线时长奖励'),('exchange','积分购买'))

    user = models.ForeignKey(User)
    type = models.CharField(max_length=20)
    brief_content = models.TextField()
    credit_change = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "积分记录"
        verbose_name_plural = verbose_name


# 积分事件绑定

#回复20,提问100,每日登陆10,签到30,在线时长满2小时+200

from forum.models import Comment , Thread
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete

@receiver(post_save,sender=Comment)
def add_comment_credit_point(sender,instance,created,**kwargs):
    if created:
        user = instance.create_user
        cs ,c = CreditStatus.objects.get_or_create(user=user)
        cs.credit_point = cs.credit_point+20
        cs.save()

        cl = CreditLog()
        cl.user = user
        cl.type = "answering"
        cl.brief_content = '您在主题下"'+instance.thread.tittle+'"评论了'+'积分+20'
        cl.credit_change = 20
        cl.save()


@receiver(post_save,sender=Thread)
def add_thread_credit_point(sender,instance,created,**kwargs):
    if created:
        user = instance.create_user
        cs ,c = CreditStatus.objects.get_or_create(user=user)
        cs.credit_point = cs.credit_point+100
        cs.save()

        cl = CreditLog()
        cl.user = user
        cl.type = "answering"
        cl.brief_content = '您创建了问题"'+instance.tittle+'",'+'积分+100'
        cl.credit_change = 100
        cl.save()

@receiver(post_delete,sender=Thread)
def delete_thread_credit_point(sender,instance,**kwargs):
    user = instance.create_user
    cs, c = CreditStatus.objects.get_or_create(user=user)
    cs.credit_point = cs.credit_point - 50
    cs.save()

    cl = CreditLog()
    cl.user = user
    cl.type = "answering"
    cl.brief_content = '您创建了问题"' + instance.tittle + '"被删除了,' + '积分-50'
    cl.credit_change = -50
    cl.save()



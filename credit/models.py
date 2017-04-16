from django.db import models

from django.contrib.auth.models import User

class UserCredit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    credit_point = models.IntegerField(default=10)
    last_modify = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "用户积分"
        verbose_name_plural = verbose_name

class UserCreditNickName(models.Model):
    name = models.CharField(max_length=10)
    start_point = models.IntegerField()
    end_point = models.IntegerField()

    # 最大最小
    index = models.IntegerField()


    class Meta:
        verbose_name = "用户积分称号"
        verbose_name_plural = verbose_name
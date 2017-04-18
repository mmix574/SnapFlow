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

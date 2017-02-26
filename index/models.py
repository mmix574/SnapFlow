from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# 用户模型扩充
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar_path = models.CharField(max_length=1024,default="")
    lang = models.CharField(max_length=10)


def create_user_profile(sender,instance,created,**kwargs):
    if(created):
        profile = UserProfile()
        profile.user = instance
        profile.save()

# 添加事件监听
post_save.connect(create_user_profile,sender=User)
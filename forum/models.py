from django.db import models
from django.contrib.auth.models import User



class Class(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    chinese_name = models.CharField(max_length=20,blank=True,null=True)
    create_user = models.ForeignKey(User,default=1,blank=True,null=True)
    create_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    pass

class SubClass(models.Model):
    parent_class = models.ForeignKey(Class)

    name = models.CharField(max_length=20)
    chinese_name = models.CharField(max_length=20)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now=True,blank=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "帖子类型"
        verbose_name_plural = verbose_name


# Create your models here.
class Thread (models.Model):
    tittle = models.CharField(max_length=20,blank=True)
    content = models.TextField(default="")
    create_user = models.ForeignKey(User,default=1)
    create_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    class Meta:

        pass

class TAG(models.Model):
    pass
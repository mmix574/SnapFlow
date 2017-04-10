from django.db import models
from django.contrib.auth.models import User



class Class(models.Model):
    name = models.CharField("name",max_length=50,blank=True,null=True)
    display_name = models.CharField("显示名字",max_length=50,null=True,blank=True)
    create_user = models.ForeignKey(User,default=1,blank=True,null=True)
    create_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    order = models.IntegerField(default=1)
    class Meta:
        verbose_name = "父帖子类型"
        verbose_name_plural = verbose_name
        ordering = ['order']
    def __str__(self):
        return self.display_name


class SubClass(models.Model):
    parent_class = models.ForeignKey(Class)
    name = models.CharField("名字",max_length=50)
    display_name = models.CharField("显示名字",max_length=50)
    # chinese_name = models.CharField(max_length=20)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now=True,blank=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = "子帖子类型"
        verbose_name_plural = verbose_name


# Create your models here.
class Thread (models.Model):
    sub_class = models.ForeignKey(SubClass,null=True)
    tittle = models.CharField(max_length=20,blank=True)
    content = models.TextField(default="")
    create_user = models.ForeignKey(User,default=1)
    create_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    last_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = verbose_name
        pass

    def __str__(self):
        return self.tittle

class Comment(models.Model):
    thread = models.ForeignKey(Thread)


    pass



class TAG(models.Model):
    pass
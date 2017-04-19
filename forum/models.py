from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    name = models.CharField("name",max_length=50,blank=True,null=True)
    display_name = models.CharField("显示名字",max_length=50,null=True,blank=True)
    create_user = models.ForeignKey(User,default=1,blank=True,null=True)
    create_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    last_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    order = models.IntegerField(default=1)
    # sub_class = models.ManyToOneRel()
    # models.ManyToManyField()

    class Meta:
        verbose_name = "父帖子类型"
        verbose_name_plural = verbose_name
        ordering = ['order']
    def __str__(self):
        return self.display_name


class SubClass(models.Model):
    parent_class = models.ForeignKey(Class)
    name = models.CharField(max_length=50)
    display_name = models.CharField("显示名字",max_length=50)
    # chinese_name = models.CharField(max_length=20)
    create_user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True,blank=True)
    last_time = models.DateTimeField(auto_now=True,blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = "子帖子类型"
        verbose_name_plural = verbose_name
        ordering = ['parent_class','order']


# Create your models here.
class Thread (models.Model):
    main_class = models.ForeignKey(Class,null=True,blank=True)
    sub_class = models.ForeignKey(SubClass,null=True,blank=True)

    tittle = models.CharField(max_length=100)
    content = models.TextField(default="",blank=True)
    # append_image = models.ImageField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    reply = models.IntegerField(default=0)
    # collection = models.IntegerField(default=0)

    # 分数
    score = models.IntegerField(default=1000)

    create_user = models.ForeignKey(User,null=False,blank=False)
    create_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    last_edit_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    last_reply_time = models.DateTimeField(null=True,blank=True)
    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = verbose_name
        pass

    def __str__(self):
        return self.tittle



from django.db.models import signals
from django.dispatch import receiver


@receiver(signals.pre_save,sender=Thread)
def before_thread_save(sender, instance, **kwargs):
    # if instance.sub_class and not instance.main_class:
    if not instance.main_class and instance.sub_class:
        # print("ready to do something")
        try:
            instance.main_class = SubClass.objects.get(id=instance.sub_class_id).parent_class
        except Exception as e:
            pass

# 评论
class Comment(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    content = models.TextField(blank=False)
    create_user = models.ForeignKey(User,related_name='thread_user')
    create_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    last_time = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return super().__str__()


class UserThreadStatus(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question_count = models.IntegerField(default=0)
    answering_count = models.IntegerField(default=0)
    being_liked_count = models.IntegerField(default=0)
    being_collected_count = models.IntegerField(default=0)
    being_disliked_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "用户状态"
        verbose_name_plural = verbose_name


class TAG(models.Model):
    thread = models.ForeignKey(Thread)
    name = models.CharField(max_length=30)
    pass

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name



class ThreadLike(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "点赞"
        verbose_name_plural = verbose_name


# event signal
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@receiver(post_save,sender=User)
def addUserThreadStatus(sender,instance,created,**kwargs):
    if created:
        uts = UserThreadStatus()
        uts.user = instance
        uts.save()

@receiver(post_save,sender=Comment)
def add_comment_count(sender,instance,created,**kwargs):
    if created:
        (ths,c) = UserThreadStatus.objects.get_or_create(user=instance.create_user)
        ths.reply_open = ths.reply_open+1
        ths.save()





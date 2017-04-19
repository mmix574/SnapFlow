from django.db import models
from django.contrib.auth.models import User


# Create your models here.


from django.contrib.auth.models import User


class MessageStatus(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_to_user_message_count = models.IntegerField(default=0)
    system_to_user_message_count = models.IntegerField(default=0)
    even_message_count = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

    @property
    def all_count(self):
        return self.user_to_user_message_count+self.system_to_user_message_count+self.even_message_count

    class Meta:
        verbose_name = "用户信息状态"
        verbose_name_plural = verbose_name


    def add_user_to_user_message_count(self):
        self.user_to_user_message_count = self.user_to_user_message_count+1
        self.save()

    def minus_user_to_user_message_count(self):
        if self.user_to_user_message_count-1 >= 0:
            self.user_to_user_message_count = self.user_to_user_message_count-1
        else:
            self.user_to_user_message_count = 0
        self.save()

    def add_system_to_user_message_count(self):
        self.system_to_user_message_count = self.system_to_user_message_count+1
        self.save()
    def minus_system_to_user_message_count(self):
        if self.system_to_user_message_count-1 >= 0:
            self.system_to_user_message_count = self.system_to_user_message_count-1
        else:
            self.system_to_user_message_count = 0
        self.save()

    def add_even_message_count(self):
        self.even_message_count = self.even_message_count+1
        self.save()
    def minus_even_message_count(self):
        if self.even_message_count-1 >= 0:
            self.even_message_count = self.even_message_count-1
        else:
            self.even_message_count = 0
        self.save()

    def clear_all(self):
        self.user_to_user_message_count = 0
        self.system_to_user_message_count = 0
        self.even_message_count = 0
        items = UserToUserMessage.objects.filter(a_user=self.user)
        for i in items:
            i.read = True
            i.save()
        items = SystemToUserMessage.objects.filter(user=self.user)
        for i in items:
            i.read = True
            i.save()
        items = EventMessage.objects.filter(user=self.user)
        for i in items:
            i.read = True
            i.save()
        self.save()



class UserToUserMessage(models.Model):
    a_user = models.ForeignKey(User,related_name="A_user",on_delete=models.CASCADE)
    b_user = models.ForeignKey(User,related_name="B_user")
    content = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    is_send = models.BooleanField(default=False)
    class Meta:
        verbose_name = "私信"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.content


class SystemToUserMessage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
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

class EventMessage(models.Model):

    types = (('being_liked',"收到赞"),('being_answering','收到答案'))

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20,choices=types)
    url = models.URLField()
    brief_content = models.CharField(max_length=80)
    read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "事件消息"
        verbose_name_plural = verbose_name

class Friend(models.Model):
    user = models.ForeignKey(User)
    has_friend = models.ForeignKey(User,related_name="myfriend")
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "好友"
        verbose_name_plural = verbose_name



from django.db.models.signals import post_save



# events
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save

@receiver(post_save,sender=User)
def create_message_status(sender,instance,created,**kwargs):
    if created:
        ms = MessageStatus()
        ms.user = instance
        ms.save()





from forum.models import ThreadLike
from forum.models import Comment


@receiver(post_save,sender=ThreadLike)
def add_event_message_thread_like(sender,instance,**kwargs):
    pass


@receiver(post_save,sender=Comment)
def add_event_message_comment(sender,instance,**kwargs):
    pass




# 2017年4月19日17:54:29
# 事件消息
@receiver(post_save,sender=EventMessage)
def add_event_message_count(sender,instance,created,**kwargs):
    if created:
        instance.user.messagestatus.add_even_message_count()

# 私信
@receiver(post_save,sender=UserToUserMessage)
def add_private_message_count(sender,instance,created,**kwargs):
    if created:
        instance.user.messagestatus.add_user_to_user_message_count()

# 系统消息
@receiver(post_save,sender=SystemToUserMessage)
def add_system_message_count(sender,instance,created,**kwargs):
    if created:
        user = instance.user
        user.messagestatus.add_system_to_user_message_count()
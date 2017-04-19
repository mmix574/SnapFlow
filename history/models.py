from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class History(models.Model):
    type_chioces = (("asking","提问"),("answering","回答"),("liking","点赞"),("collecting","收藏"),("commenting","回答"))

    user = models.ForeignKey(User)
    type = models.CharField(max_length=20,choices=type_chioces)
    brief_content = models.CharField(max_length=60)
    url = models.URLField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    @property
    def ctype(self):
        return self.get_type_display()

    def __str__(self):
        return self.user.username+"-->"+self.type+":"+self.brief_content

    class Meta:
        verbose_name = "历史"
        verbose_name_plural = verbose_name



# event receive

from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver


from forum.models import ThreadLike
@receiver(post_save,sender=ThreadLike)
def add_like(sender,instance,created,**kwargs):
    if created:
        h = History()
        h.type = "liking"
        h.user = instance.user
        h.brief_content = instance.thread.tittle
        h.url='/t/'+str(instance.thread.id)
        h.save()

from forum.models import Thread
@receiver(post_save,sender=Thread)
def add_thread_history(sender,instance,created,**kwargs):
    if created:
        h = History()
        h.type = "asking"
        h.brief_content = instance.tittle
        h.user = instance.create_user
        h.url = '/t/'+str(instance.id)
        h.save()

from forum.models import Comment
@receiver(post_save,sender=Comment)
def add_comment_history(sender,instance,created,**kwargs):
    if created:
        h = History()
        h.type = "answering"
        h.brief_content = instance.content
        h.user = instance.create_user
        h.url = '/t/'+str(instance.thread.id)
        h.save()

from collection.models import Collection
@receiver(post_save,sender=Collection)
def add_collection_history(sender,instance,created,**kwargs):
    if created:
        h = History()
        h.type="collecting"
        h.brief_content = instance.thread.tittle
        h.user=instance.create_user
        h.url = '/t/'+str(instance.thread.id)
        h.save()
















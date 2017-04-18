from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class History(models.Model):
    type_chioces = (("asking","提问"),("answering","回答"),("liking","点赞"),("collecting","收藏"))

    user = models.ForeignKey(User)
    type = models.CharField(max_length=20,choices=type_chioces)
    brief_content = models.CharField(max_length=60)
    url = models.URLField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "历史"
        verbose_name_plural = verbose_name

# event receive

from django.db.models.signals import post_save
from django.dispatch import receiver


from forum.models import ThreadLike
@receiver(post_save,sender=ThreadLike)
def add_like(sender,instance,created,**kwargs):
    if created:
        h = History()
        h.type = "liking"
        h.user = instance.user
        h.brief_content = instance.thread.tittle
        h.save()

from django.db import models

# Create your models here.



class History(models.Model):
    class Meta:
        verbose_name = "历史"
        verbose_name_plural = verbose_name
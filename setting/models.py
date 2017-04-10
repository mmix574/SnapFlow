from django.db import models

# Create your models here.


class SystemEmailInfo(models.Model):
    email_address = models.CharField(max_length=255)
    name = models.CharField(default="admin",max_length=20)
    port = models.IntegerField()
    protocal = models.CharField(max_length=20)
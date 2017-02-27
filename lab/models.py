from django.db import models

# Create your models here.

class AddModel(models.Model):
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    result = models.IntegerField(null=True)

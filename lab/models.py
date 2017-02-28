from django.db import models

# Create your models here.

class AddModel(models.Model):
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    result = models.IntegerField(null=True)




from django.contrib.auth.models import User

class PostModel(models.Model):
    tittle = models.CharField(max_length=30)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.tittle

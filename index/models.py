from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = ModelWithFileField(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})


from django.conf import settings


class UserProfileManager(models.Manager):
    def givemeabool(self):
        return True


# 用户模型扩充
from os import path
def upload_to(instance,filename):

    filename,filetype = filename.split('.')
    _= path.join("ava",str(instance.user.id)+'.'+filetype)
    print(_)
    return _


def default_avatar():
    return "/default-user-image.png"

class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(default=default_avatar,null=True,blank=True,upload_to=upload_to)
    # set_avatar = models.BooleanField(default=False)
    # avatar = models.ImageField(null=True,blank=True)
    work_year = models.IntegerField("工作年限",default=0,blank=True)
    work_place = models.CharField("工作单位",max_length=20,blank=True)
    work_nickname = models.CharField("职位",max_length=20,blank=True)
    language = models.CharField("使用语言",max_length=10,blank=True)
    self_introduction = models.CharField("自我介绍",max_length=300,blank=True)
    blog_adderss = models.URLField(blank=True)

    objects = UserProfileManager()

    def __str__(self):
        return "[userprofile@user_id:"+str(self.user.id)+" username:"+self.user.username+"]"



# class UserProfileManager(models.Manager):
#     def givemeabool(self):
#         return True

def create_user_profile(sender,instance,created,**kwargs):
    if(created):
        profile = UserProfile()
        profile.user = instance
        profile.save()

# 添加事件监听
post_save.connect(create_user_profile,sender=User)
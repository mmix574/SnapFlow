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


# 用户模型扩充
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    lang = models.CharField(max_length=10,null=True,blank=True)
    avatar = models.ImageField(null=True,blank=True,upload_to='cat/')



def create_user_profile(sender,instance,created,**kwargs):
    if(created):
        profile = UserProfile()
        profile.user = instance
        profile.save()

# 添加事件监听
post_save.connect(create_user_profile,sender=User)
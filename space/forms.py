from website.utils import console
from django import forms
from django.contrib.auth.models import User
from index.models import UserProfile

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','first_name']

    # def clean_first_name(self):
    #     first_name = self.clean_first_name()
    #     # raise forms.ValidationError("呵呵  ...")
    #     return first_name

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['id','work_place','work_nickname','language','self_introduction']


    #     avatar = models.ImageField(null=True,blank=True,upload_to='cat/')
    # work_place = models.CharField(max_length=20)
    # work_nickname = models.CharField(max_length=20)
    # lang = models.CharField(max_length=10,null=True,blank=True)


class UserAvatarForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['avatar']
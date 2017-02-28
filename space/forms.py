from django import forms


from django.contrib.auth.models import User
from index.models import UserProfile

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['avatar','work_place','work_nickname','language']



    #     avatar = models.ImageField(null=True,blank=True,upload_to='cat/')
    # work_place = models.CharField(max_length=20)
    # work_nickname = models.CharField(max_length=20)
    # lang = models.CharField(max_length=10,null=True,blank=True)

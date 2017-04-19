from website.utils import console
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.models import User
from space.forms import UserForm

from index.appviews import AppBaseTemplateView
from space.forms import UserProfileForm
from index.models import UserProfile
from space.forms import UserAvatarForm


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserForm

from website.utils import console
from website.utils import messages





@method_decorator(login_required,name='dispatch')
class UserDataView(AppBaseTemplateView):
    template_name = "space/userdata.html"
    def get(self, request,context={}, *args, **kwargs):
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
        user_avatar_form = UserAvatarForm(instance=request.user.userprofile)

        return super(UserDataView, self).get(request,context={"user_form":user_form,"user_profile_form":user_profile_form,"user_avatar_form":user_avatar_form}, *args, **kwargs)


    def post(self,request,context={},*args,**kwargs):

        form_name = request.POST.get('form_name',None)

        if form_name == "user_avatar_form":
            uaf = UserAvatarForm(request.POST,request.FILES,instance=request.user.userprofile)
            if uaf.is_valid():
                uaf.save()
        elif form_name == 'user_data':
            uaf = UserProfileForm(request.POST, instance=request.user.userprofile)
            if uaf.is_valid():
                uaf.save()

            instance = User.objects.get(id=request.user.id)
            uf = UserForm(request.POST,instance=instance)
            # real_user = User.objects.get(id=request.user.id)
            # if request.POST.get('first_name',None):
            #     real_user.first_name = request.POST.get('first_name',None)
            #     real_user.save()
            # else:
            #     print("something wrong")

            print(uf)

            if uf.is_valid():
                uf.save()
            else:
                print(uf.errors)

        elif form_name == 'password_changing':
            print('password_changing')
            pass
        elif form_name =='email_changing':
            user = User.objects.get(id=request.user.id)
            if request.POST.get('email',None):
                user.email = request.POST.get('email',None)
                user.save()


        instance = User.objects.get(id=request.user.id)
        user_form = UserForm(instance=instance)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
        user_avatar_form = UserAvatarForm(instance=request.user.userprofile)

        return super(UserDataView, self).post(request,context={"user_form":user_form,"user_profile_form":user_profile_form,"user_avatar_form":user_avatar_form},*args,**kwargs)



from forum.models import UserThreadStatus
@method_decorator(login_required,name='dispatch')
class UserProfileView(AppBaseTemplateView):
    template_name = 'space/userprofile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_thread_status  = UserThreadStatus.objects.get(user=self.request.user)
        context['user_thread_status'] = user_thread_status
        return context

    def get(self, request, context={}, *args, **kwargs):

        return super().get(request, context, *args, **kwargs)


@method_decorator(login_required,name='dispatch')
class UserAchieveView(AppBaseTemplateView):
    template_name = 'space/userachieve.html'





















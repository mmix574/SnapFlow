from website.utils import console
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def default(request):
    return HttpResponseRedirect('/space/member/')

def member(request):
    # return HttpResponse("hello member...")
    return render(request,"space/member.html",{"tittle":"hello world","user":request.user})

from django.views.generic.base import TemplateView

# @method_decorator(csrf_exempt, name='dispatch')
# class MemberView(TemplateView):
#     template_name = 'space/member.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MemberView,self).get_context_data(**kwargs)
#         context['tittle'] = "hello world!"
#         return context
#
#     def get(self, request, *args, **kwargs):
#         print("get view from parent!")
#         return super().get(self,request,*args,**kwargs)


from django.conf import settings
from index.appviews import AppBaseTemplateView

from django.contrib.auth.models import User
from space.forms import UserForm
from space.forms import UserProfileForm
from index.models import UserProfile
from space.forms import UserAvatarForm


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User

@method_decorator(login_required,name='dispatch')
class MemberView(AppBaseTemplateView):
    template_name = "space/member.html"

    def get(self, request, *args, **kwargs):
        up = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(instance=up)
        return super(MemberView, self).get(request,context={"form":form},*args,**kwargs)


    def post(self,request,*args,**kwargs):
        up = UserProfile.objects.get(user=request.user)
        from website.utils import console
        # console.log(request.POST)
        # console.log(request.FILES)

        form = UserProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        # model = form.save(commit=False)
        # model.user = request.user
        # model.id = up.id
        # model.save()
        #
        # up = UserProfile.objects.get(user=request.user)
        # form = UserProfileForm(instance=up)
        if form.is_valid():
            form.save()

        form = UserProfileForm(instance=request.user.userprofile)

        return super(MemberView, self).post(request,context={"form":form},*args,**kwargs)



from django.contrib.auth.models import User
from website.utils import console
from website.utils import messages


class UserDataView(AppBaseTemplateView):
    template_name = "space/userdata.html"

    def get(self, request,context={}, *args, **kwargs):

        # console.log()

        form1 = UserForm(instance=request.user)
        form2 = UserProfileForm(instance=request.user.userprofile)
        form3 = UserAvatarForm(instance=request.user.userprofile)

        tab_name = "tab1"
        return super(UserDataView, self).get(request,context={"form1":form1,"form2":form2,"form3":form3,"tab_name":tab_name}, *args, **kwargs)


    def post(self,request,context={},*args,**kwargs):

        form1 = UserForm(instance=request.user,data=request.POST)
        form2 = UserProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        form3 = UserAvatarForm(request.POST,request.FILES,instance=request.user.userprofile)


        # form1 = UserForm(instance=request.user)
        # form2 = UserProfileForm(instance=request.user.userprofile)
        # form3 = UserAvatarForm(instance=request.user.userprofile)

        tab_name = request.POST.get("tab_name","tab1")

        if tab_name=="tab1":
            if form1.is_valid():
                form1.save()
            else:
                console.log("form1 invalidate")
            pass
            if form2.is_valid():
                form2.save()
            else:
                console.log("form2 invalidate")
            pass

        if tab_name=="tab2":
            if form3.is_valid():
                form3.save()
                form3 = UserAvatarForm(instance=request.user.userprofile)
            else:
                console.log("form3 invalidate")
            pass
        if tab_name=="tab3":
            pass


        form1 = UserForm(instance=request.user)
        form2 = UserProfileForm(instance=request.user.userprofile)
        form3 = UserAvatarForm(instance=request.user.userprofile)

        return super(UserDataView, self).post(request,context={"form1":form1,"form2":form2,"form3":form3,"tab_name":tab_name},*args,**kwargs)


class UserHomePageView(AppBaseTemplateView):
    pass
























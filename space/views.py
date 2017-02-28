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

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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

        form = UserProfileForm(request.POST,request.FILES)
        model = form.save(commit=False)
        model.user = request.user
        model.id = up.id
        model.save()

        up = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(instance=up)

        return super(MemberView, self).post(request,context={"form":form},*args,**kwargs)



class UserDataView(AppBaseTemplateView):
    template_name = "space/userdata.html"
























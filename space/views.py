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

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required,name='dispatch')
class MemberView(AppBaseTemplateView):
    template_name = "space/member.html"

    def get_context_data(self, **kwargs):
        context = super(MemberView, self).get_context_data()
        user = context['user']
        context['form'] = UserForm(instance=user)
        return context

    def get(self, request, *args, **kwargs):
        return super(MemberView, self).get(request,*args,**kwargs)


    def post(self,request,*args,**kwargs):
        return super(MemberView, self).post(request,*args,**kwargs)




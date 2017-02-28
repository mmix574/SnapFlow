from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect


from django.views.generic.base import TemplateView
from django.views.generic.base import View

from django.http import JsonResponse
from django.template.response import TemplateResponse



from .appviews import AppBaseTemplateView

class IndexView(AppBaseTemplateView):
    template_name = 'index/index.html'
    pass

class MessageView(AppBaseTemplateView):

    tittle = ""
    message = ""

    template_name = 'index/message.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(self.message):
            context['message_content'] =self.message
        else:
            context['message_content'] = "you should pass 'message_content' parameter to the as_view() function"
        if(self.tittle):
            context['message_tittle'] = self.tittle
        else:
            context['message_tittle'] = "Alarm"
        return context



from website.utils import console

def login(request):
    context = {"tittle":"登陆","loginpage":True}
    if(request.method=='GET'):
        if request.GET.get('next',None):
            context['next'] = request.GET.get('next',None)
            pass
        pass
    elif(request.method=='POST'):
        from django.contrib import auth
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = auth.authenticate(username=username,password=password)

        if(user):
            auth.login(request,user)
            next = request.GET.get("next",None)
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect('/')
        else:
            pass
        pass
    else:
        pass

    return render(request,'index/login.html',context)


class LogoutView(TemplateView):
    template_name = 'index/logout.html'
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return MessageView.as_view(tittle="退出成功",message="你已经完全登出，没有任何个人信息留在这台电脑上。")(request)

def register(request):
    if(request.method=='GET'):
        pass
    elif(request.method=="POST"):
        pass
    else:
        pass

    return render(request,'index/register.html')

def about(request):
    return render(request,'index/about.html')



@login_required
def username(request):
    from django.contrib.auth.models import User
    user = User.objects.filter(username=request.user.username)
    print(user[0].email)

    return HttpResponse("你好,"+user[0].username+" "+user[0].email)


def dologin(request):
    user = auth.authenticate(username='mmix',password='mm5201314')
    if(user):
        print('ready to login')
        auth.login(request,user)
        pass
    else:
        print('password incorrect')
        pass
    return HttpResponse("...logining...")


class PasswordChangeView(AppBaseTemplateView):
    template_name = 'index/passwordchange.html'




class TestView(TemplateView):
    template_name = 'index/test.html'
    def get(self, request, *args, **kwargs):

        # from django.contrib.auth.models import User
        resp = {"trythis":None}

        return JsonResponse(resp)

        return HttpResponse("Testing... 请继续Debug.")

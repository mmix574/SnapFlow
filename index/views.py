from django.shortcuts import render


from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


from django.views.generic.base import TemplateView
from django.views.generic.base import View

from django.http import JsonResponse
from django.template.response import TemplateResponse



from website.views import AppBaseTemplateView

class IndexView(AppBaseTemplateView):
    template_name = 'index/index.html'
    pass

class MessageView(AppBaseTemplateView):
    template_name = 'index/message.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_tittle'] = "Message Tittle"
        context['message_content'] = "Message Content"
        return context

class TestView(TemplateView):
    template_name = 'index/test.html'
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request,'index/test.html',{"content":"那你他妈的很吊哦"})
        # return JsonResponse(data={})
        # return super(TestView, self).get(request,args,kwargs)

def login(request):
    if(request.method=='GET'):
        pass
    elif(request.method=='POST'):
        from django.contrib import auth
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = auth.authenticate(username=username,password=password)
        if(user):
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            pass
        pass
    else:
        pass

    return render(request,'index/login.html',{'tittle':"登陆"})

def logout(request):
    auth.logout(request)
    return render(request,'index/logout.html')


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
    return HttpResponse("你好,"+request.user.username)


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

def test(request):
    # return HttpResponse("")
    return MessageView.as_view()(request)
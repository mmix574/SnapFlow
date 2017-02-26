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



from .appviews import AppBaseTemplateView

class IndexView(AppBaseTemplateView):
    template_name = 'index/index.html'
    pass

class MessageView(AppBaseTemplateView):
    message = ""
    template_name = 'index/message.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_content'] =self.message
        return context

class TestView(TemplateView):
    template_name = 'index/test.html'
    def get(self, request, *args, **kwargs):
        # from .appresponse import AppMessageResponse
        # return AppMessageResponse()

        # this is something you want 2017年2月26日 22:02:10
        return MessageView.as_view(message="hello world")(request)
        # return TemplateResponse(request,'index/test.html',{"content":"那你很棒哦"})
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

def test(request):
    # return HttpResponse("")
    from .appresponse import AppMessageResponse
    return AppMessageResponse()
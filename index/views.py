from django.shortcuts import render


from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def index(request):
    userdata = {}
    if(request.user.is_authenticated()):
        userdata = {"username":request.user}
        pass
    else:
        pass
    return render(request,'index/index.html',{'tittle':"首页","userdata":userdata})


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

def error(request):
    return render(request,'index/error.html')

def message(request):
    return render(request,'index/message.html')

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
    return HttpResponseRedirect('/')
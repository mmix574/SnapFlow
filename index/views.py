from django.shortcuts import render


from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    userdata = {}
    if(request.user.is_authenticated()):
        userdata = {"username":request.user}
        pass
    else:
        pass
    return render(request,'index/index.html',{'tittle':"首页","userdata":userdata})

def login(request):
    from django.contrib import auth
    from django.contrib.auth import authenticate
    user = authenticate(username="test",password ="test123")

    auth.login(request,user)

    return render(request,'index/login.html')

def logout(request):

    return render(request,'index/logout.html')

def error(request):
    return render(request,'index/error.html')

def message(request):
    return render(request,'index/message.html')

def register(request):
    if(request.method=='GET'):
        pass
    elif(request.method=="POST"):
        print("checking user")
        pass
    else:
        pass

    return render(request,'index/register.html')

def about(request):
    return render(request,'index/about.html')

# add test methods here
def test(request):
    from django.contrib.auth.models import User
    return HttpResponse("testing...")
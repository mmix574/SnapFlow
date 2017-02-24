from django.shortcuts import render


from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    # return HttpResponse("<h1>hello world</h1>")
    return render(request,'index/index.html',{'tittle':"首页"})

def login(request):
    return render(request,'index/login.html')

def logout(request):
    return render(request,'index/logout.html')

def error(request):
    return render(request,'index/error.html')

def message(request):
    return render(request,'index/message.html')

def register(request):
    return render(request,'index/register.html')

def about(request):
    return render(request,'index/about.html')
from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("<h1>hello world</h1>")
    return render(request,'index/index.html',{'tittle':"首页"})

def login(request):
    return render(request,'index/login.html')
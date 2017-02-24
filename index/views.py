from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("<h1>hello world</h1>")
<<<<<<< HEAD
    return render(request,'index/index.html',{'tittle':"首页"})

def login(request):
    return render(request,'index/login.html')
=======
    return render(request,'index/index.html',{'tittle':"homepage"})
>>>>>>> f332e73866a28c53bec7ffb3263e1776783d1a05

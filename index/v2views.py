from django.shortcuts import render
from django.views.generic import TemplateView
from . import views as V1View


class V2Index(TemplateView):
    template_name = 'v2index/w.html'

    def get_context_data(self, **kwargs):
        return super(V2Index, self).get_context_data(**kwargs)


    def get(self, request, *args, **kwargs):
        return super(V2Index, self).get( request, *args, **kwargs)



class RegisterView(TemplateView):
    template_name = "v2index/w.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs);
        context['view'] = "register"
        return context




from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from website.utils import console
class LoginView(TemplateView):
    template_name = "v2index/w.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs);
        context['view'] = "login"
        return context
    
    def get(self, request, *args, **kwargs):
        return super(LoginView, self).get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return super(LoginView, self).post(request, *args, **kwargs)
    def post(self,request):
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
            else:
               return V1View.MessageView.as_view(tittle="用户名或者密码不正确",message="你输入的账号密码似乎有些不正确，请重试。")(request)

        else:
            return V1View.MessageView.as_view(tittle="用户名与密码请求不完整", message="如果多次出现这个提示，请联系管理员")(request)

        return HttpResponseRedirect("/");

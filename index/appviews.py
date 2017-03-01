from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse

from django.views.generic.base import TemplateView

from django.contrib.auth.models import AnonymousUser

from website.utils import console
class AppBaseTemplateView(TemplateView):


    # 子类调用User 与 Request 的方法:
    # user = context['user']
    # request = context['request']
    # 所有的request 参数都在context['request'] 中

    def get_context_data(self, **kwargs):
        # 子类可以通过父类的get_context_data 继续添加context数据
        context = super().get_context_data()
        context["tittle"] = "AppBaseTemplateView -- DEBUG"

        # 判断用户是否已经登陆
        request = self.request
        if request.user.is_authenticated:
            context['logined'] = True
        else:
            context['logined'] = False

        context.update(self.__additional_data)
        return context

    def get(self, request,context={}, *args, **kwargs):
        self.__additional_data = {}
        self.__additional_data['user'] = request.user
        self.__additional_data['request'] = request
        if(context):
            self.__additional_data.update(context)
        # return super().get(request,*args,**kwargs)
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,context={},*args,**kwargs):
        self.__additional_data = {}
        self.__additional_data['user'] = request.user
        self.__additional_data['request'] = request
        if(context):
            self.__additional_data.update(context)
        return render(request,self.template_name,self.get_context_data())


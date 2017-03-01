from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse

from django.views.generic.base import TemplateView

from django.contrib.auth.models import AnonymousUser

from website.utils import console


def get_ctime():
    import datetime
    now = datetime.datetime.now()
    if (now.hour >= 18 or now.hour < 6):
        return  "晚上好,"
    elif (now.hour >= 6 and now.hour < 12):
        return "早上好,"
    else:
        return "下午好,"

class AppBaseTemplateView(TemplateView):
    __additional_data = {}

    # 子类调用User 与 Request 的方法:
    # user = context['user']
    # request = context['request']
    # 所有的request 参数都在context['request'] 中
    # 可用关键子:
    # 2017年3月1日 20:35:28
    # request,user,profile,logined,tittle
    #
    def get_context_data(self, **kwargs):
        # 子类可以通过父类的get_context_data 继续添加context数据
        context = super().get_context_data()
        context["tittle"] = "AppBaseTemplateView -- DEBUG"

        # 判断用户是否已经登陆
        request = self.request
        if request.user.is_authenticated:
            context['logined'] = True

            context['user'] = request.user
            context['profile'] = request.user.userprofile

        else:
            context['logined'] = False


        # 公用数据
        context['request'] = request
        context['ctime'] = get_ctime()

        return context


    #donot edit 2017年3月1日 20:51:23
    def get(self, request,context={}, *args, **kwargs):
        c = self.get_context_data()
        c.update(context)
        return render(request, self.template_name, c)
    def post(self,request,context={},*args,**kwargs):
        c = self.get_context_data()
        c.update(context)
        return render(request,self.template_name,c)


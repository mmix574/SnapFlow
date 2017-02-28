from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse

from django.views.generic.base import TemplateView

class AppBaseTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["tittle"] = "AppBaseTemplateView -- DEBUG"
        context.update(self.__additional_data)
        return context;

    def get(self, request, *args, **kwargs):

        self.__additional_data = {}
        if request.user.is_authenticated():
            self.__additional_data['logined'] = True
            user = dict()
            user['username'] = request.user.username
            user['is_staff'] = request.user.is_staff

            self.__additional_data['user'] = user
        else:
            self.__additional_data['logined'] = False

        return super().get(request,*args,**kwargs)


# 继承后在get 之前执行执行super.get
# super.post
# super.contexy data

    def render_to_response(self, context, **response_kwargs):
        return super().render_to_response(context, **response_kwargs)


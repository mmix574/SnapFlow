from django.shortcuts import render
from django.views.generic import TemplateView

from index.appviews import AppBaseTemplateView
from django.shortcuts import get_object_or_404

from .models import Class
from .models import SubClass
from .models import Thread

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from website.contrib.response import MessageResponse

# 定义默认tab
def get_default_tab():
    return "technique"

class IndexView(AppBaseTemplateView):
    template_name = 'forum/index.html'

    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        return super().post(request, context, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        display_class = Class.objects.all().order_by('order')
        if not (len(context)):
            return MessageResponse("提示","没有任何的ThreadType，请在数据库中先添加")
        context['display_class'] = display_class

        tab = self.request.GET.get('tab',get_default_tab())
        context['tab'] = tab
        tab_instance = Class.objects.filter(name=tab)
        if not tab_instance:
            return context

        display_sub_class = SubClass.objects.filter(parent_class=tab_instance[0])
        if not display_sub_class:
            return context
        context['display_sub_class'] = list(display_sub_class)

        subtab = self.request.GET.get('subtab',None)

        content_list = {}
        if tab and subtab:
            subtab_instance = SubClass.objects.get(name=subtab)
            content_list = Thread.objects.filter(main_class=tab_instance,sub_class=subtab_instance)
        elif tab:
            content_list = Thread.objects.filter(main_class=tab_instance)


        # print(content_list)
        context['content_list'] = content_list

        return context
@method_decorator(login_required,name='dispatch')
class CreateView(AppBaseTemplateView):
    template_name = 'forum/create.html'




class SearchView(AppBaseTemplateView):
    template_name = 'forum/search.html'

class DetailView(AppBaseTemplateView):
    template_name = 'forum/detail.html'


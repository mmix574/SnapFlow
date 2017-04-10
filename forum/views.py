from django.shortcuts import render
from django.views.generic import TemplateView

from index.appviews import AppBaseTemplateView
from django.shortcuts import get_object_or_404

from .models import Class
from .models import SubClass


from website.contrib.response import MessageResponse

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

        tab = self.request.GET.get('tab',"technique")
        context['tab'] = tab


        return context


class CreateView(AppBaseTemplateView):
    template_name = 'forum/create.html'

class NewView(AppBaseTemplateView):
    template_name = 'forum/new.html'


class SearchView(AppBaseTemplateView):
    template_name = 'forum/search.html'
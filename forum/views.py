from django.shortcuts import render
from django.views.generic import TemplateView

from index.appviews import AppBaseTemplateView


from .models import Class


class IndexView(AppBaseTemplateView):
    template_name = 'forum/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        display_class = Class.objects.all().order_by('order')
        context['display_class'] = display_class
        return context





class CreateView(AppBaseTemplateView):
    template_name = 'forum/create.html'

class NewView(AppBaseTemplateView):
    template_name = 'forum/new.html'


class SearchView(AppBaseTemplateView):
    template_name = 'forum/search.html'
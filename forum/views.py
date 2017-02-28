from django.shortcuts import render
from django.views.generic import TemplateView

from index.appviews import AppBaseTemplateView


# Create your views here.

class IndexView(AppBaseTemplateView):
    template_name = 'forum/index.html'


class CreateView(AppBaseTemplateView):
    template_name = 'forum/create.html'

class NewView(AppBaseTemplateView):
    template_name = 'forum/new.html'


class SearchView(AppBaseTemplateView):
    template_name = 'forum/search.html'
from django.shortcuts import render
from django.views.generic import TemplateView

from index.appviews import AppBaseTemplateView


# Create your views here.

class IndexView(AppBaseTemplateView):
    template_name = 'forum/index.html'

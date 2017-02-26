from django.shortcuts import render

# Create your views here.

from index.appviews import AppBaseTemplateView

class IndexView(AppBaseTemplateView):
    template_name = 'timeline/index.html'

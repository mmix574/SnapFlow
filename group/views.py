from django.shortcuts import render
from index.views import AppBaseTemplateView

# Create your views here.


class IndexView(AppBaseTemplateView):
    template_name = 'group/index.html'
    pass



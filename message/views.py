from django.shortcuts import render
from index.appviews import AppBaseTemplateView

# Create your views here.


class IndexView(AppBaseTemplateView):
    template_name = 'message/index.html'





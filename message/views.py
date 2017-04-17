from django.shortcuts import render
from index.appviews import AppBaseTemplateView

# Create your views here.


class IndexView(AppBaseTemplateView):
    template_name = 'message/system_message.html'




class SystemMessageView(AppBaseTemplateView):
    template_name = 'message/system_message.html'

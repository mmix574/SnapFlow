from django.shortcuts import render
from index.appviews import AppBaseTemplateView

# Create your views here.


class EventMessageView(AppBaseTemplateView):
    template_name = 'message/event.html'


class SystemMessageView(AppBaseTemplateView):
    template_name = 'message/system.html'


class UserToUserView(AppBaseTemplateView):
    template_name = 'message/chat.html'



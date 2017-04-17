from django.shortcuts import render
from index.appviews import AppBaseTemplateView
from  django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


from django.http.response import HttpResponseRedirect


@method_decorator(login_required,name="dispatch")
class IndexView(AppBaseTemplateView):
    template_name = 'message/__index.html'

    def get(self, request, context={}, *args, **kwargs):
        return HttpResponseRedirect('/m/message-status')


@method_decorator(login_required,name="dispatch")
class SystemMessageView(AppBaseTemplateView):
    template_name = 'message/system_message.html'

@method_decorator(login_required,name="dispatch")
class PrivateMessageView(AppBaseTemplateView):
    template_name = 'message/private_message.html'







from django.contrib.auth.models import User
from .models import UserMessageStatus


@method_decorator(login_required,name="dispatch")
class MessageStatusView(AppBaseTemplateView):
    template_name = 'message/message_status.html'

    def get(self, request, context={}, *args, **kwargs):
        user = request.user
        ums, created = UserMessageStatus.objects.get_or_create(user=user)
        context["user_message_status"] = ums
        return super().get(request, context, *args, **kwargs)


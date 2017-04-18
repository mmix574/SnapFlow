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





from .models import SystemToUserMessage
@method_decorator(login_required,name="dispatch")
class SystemMessageView(AppBaseTemplateView):
    template_name = 'message/system_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sm = SystemToUserMessage.objects.filter(user=self.request.user)
        context['system_message'] = sm
        return context

    def get(self, request, context={}, *args, **kwargs):

        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        return super().post(request, context, *args, **kwargs)


@method_decorator(login_required,name="dispatch")
class PrivateMessageView(AppBaseTemplateView):
    template_name = 'message/private_message.html'



from django.contrib.auth.models import User
from .models import UserMessageStatus


@method_decorator(login_required,name="dispatch")
class MessageStatusView(AppBaseTemplateView):
    template_name = 'message/message_status.html'

    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        operation = request.POST.get('operation',None)
        if not operation:
            return super().post(request, context, *args, **kwargs)

        if operation=="clear":
            ums, created = UserMessageStatus.objects.get_or_create(user=request.user)
            ums.user_to_user_message_count = 0
            ums.system_to_user_message_count = 0
            ums.even_message_count = 0;
            ums.save()
            pass



        return super().post(request, context, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ums, created = UserMessageStatus.objects.get_or_create(user=self.request.user)
        context["user_message_status"] = ums
        return context

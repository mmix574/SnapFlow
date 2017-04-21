from django.shortcuts import render
from index.appviews import AppBaseTemplateView
from  django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


from django.http.response import HttpResponseRedirect

# models
from django.contrib.auth.models import User
from .models import SystemToUserMessage
from .models import UserToUserMessage

@method_decorator(login_required,name="dispatch")
class IndexView(AppBaseTemplateView):
    template_name = 'message/__index.html'

    def get(self, request, context={}, *args, **kwargs):
        return HttpResponseRedirect('/m/system-message')


from .models import SystemToUserMessage
@method_decorator(login_required,name="dispatch")
class SystemMessageView(AppBaseTemplateView):
    template_name = 'message/system_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sm = SystemToUserMessage.objects.filter(user=self.request.user).order_by('-time')
        context['system_message'] = sm
        return context

    def get(self, request, context={}, *args, **kwargs):

        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        print(request.POST)
        operation = request.POST.get("operation",None)
        ids = request.POST.getlist("_id",None)

        if not operation or not ids:
            return super().post(request, context, *args, **kwargs)

        if operation=="read":
            for i in ids:
                try:
                    stum = SystemToUserMessage.objects.get(id=i,user=request.user)
                    if not stum.read:
                        request.user.messagestatus.minus_system_to_user_message_count()
                    stum.read = True
                    stum.save()
                except Exception as e:
                    pass
                pass
        elif operation=="unread":
            for i in ids:
                try:
                    stum = SystemToUserMessage.objects.get(id=i,user=request.user)
                    if stum.read:
                        request.user.messagestatus.add_system_to_user_message_count()
                    stum.read = False
                    stum.save()
                except Exception as e:
                    pass
        elif operation=="delete":
            for i in ids:
                try:
                    stum = SystemToUserMessage.objects.get(id=i, user=request.user)
                    print(stum)
                    stum.delete()
                except Exception as e:
                    pass
            pass

        return super().post(request, context, *args, **kwargs)


from .models import UserToUserMessageSession
@method_decorator(login_required,name="dispatch")
class PrivateMessageView(AppBaseTemplateView):
    template_name = 'message/private_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        u2u_list = UserToUserMessage.objects.filter(a_user=self.request.user)
        context['u2u_list'] = u2u_list

        session_list = UserToUserMessageSession.objects.filter(a_user=self.request.user)
        context['session_list'] = session_list
        return context

    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        return super().post(request, context, *args, **kwargs)


from .models import MessageStatus


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
            ums = request.user.messagestatus
            ums.clear_all()


        return super().post(request, context, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ums, created = MessageStatus.objects.get_or_create(user=self.request.user)
        context["user_message_status"] = ums
        return context

from .models import EventMessage
@method_decorator(login_required,name="dispatch")
class EventMessageView(AppBaseTemplateView):
    template_name = 'message/event_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_message_list = EventMessage.objects.filter(user=self.request.user).order_by('-time')
        context['event_message_list'] = event_message_list
        return context

    def post(self, request, context={}, *args, **kwargs):
        operation = request.POST.get('operation',None)
        ids = request.POST.getlist('ids',None)

        if operation=='read':
            for i in ids:
                try:
                    msg = EventMessage.objects.get(user=request.user,id=i)
                    if not msg.read:
                        request.user.messagestatus.minus_even_message_count()
                        pass
                    msg.read = True
                    msg.save()
                except Exception as e:
                    pass
        elif operation=='unread':
            for i in ids:
                try:
                    msg = EventMessage.objects.get(user=request.user,id=i)
                    if msg.read:
                        request.user.messagestatus.add_even_message_count()
                    msg.read = False
                    msg.save()
                except Exception as e:
                    pass
        elif operation=='delete':
            for i in ids:
                try:
                    msg = EventMessage.objects.get(user=request.user, id=i)
                    msg.delete()
                except Exception as e:
                    pass
            pass

        return super().post(request, context, *args, **kwargs)


@method_decorator(login_required,name="dispatch")
class FriendView(AppBaseTemplateView):
    template_name = 'message/friends.html'
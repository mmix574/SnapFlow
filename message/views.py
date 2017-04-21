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
from .models import Friend
@method_decorator(login_required,name="dispatch")
class PrivateMessageView(AppBaseTemplateView):
    template_name = 'message/private_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        u2u_list = UserToUserMessage.objects.filter(a_user=self.request.user)
        context['u2u_list'] = u2u_list

        session_list = UserToUserMessageSession.objects.filter(a_user=self.request.user)
        context['session_list'] = session_list


        session_open = True
        u = self.request.GET.get('u',None)
        has_u_input = u
        context['has_u_input'] = has_u_input
        if not u:
            session_open = False
            return context
        session_users = User.objects.filter(username=u)
        if not session_users:
            session_open = False
            return context

        chatting_user = session_users[0]
        context['chatting_user'] = chatting_user

        return context

    def get(self, request, context={}, *args, **kwargs):
        # 这里添加好友。

        u = request.GET.get('u',None)
        if not u:
            return super().get(request, context, *args, **kwargs)

        try:
            has_friend = User.objects.get(username=u)
            if not has_friend:
                return super().get(request, context, *args, **kwargs)

            relationship = Friend.objects.filter(user=request.user,has_friend=has_friend)

            if not relationship:
                f = Friend()
                f.user = request.user
                f.has_friend = has_friend
                f.save()

        except:
            pass


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


from django.contrib.auth.models import User
from django.db.models import Q
@method_decorator(login_required,name="dispatch")
class FriendView(AppBaseTemplateView):
    template_name = 'message/friends.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 获取好友列表
        friend_list =  Friend.objects.filter(user=self.request.user).order_by('-create_time')

        context['friend_list'] = friend_list

        return context

    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):

        print(request.POST)

        operation = request.POST.get('operation',None)
        if not operation:
            return super().post(request, context, *args, **kwargs)

        if operation=='search_friend':
            friend_name = request.POST.get('friend_name',None)
            if not friend_name:
                return super().post(request, context, *args, **kwargs)

            search_user_list = User.objects.filter(Q(username__contains=friend_name),~Q(id=self.request.user.id))
            context['friend_name'] = friend_name
            context['search_user_list'] = search_user_list
            if not search_user_list:
                context['search_result_statement'] = "没有查找到用户"
            else:
                context['search_result_statement'] = "一共查找到"+str(len(search_user_list))+" 名用户"

        if operation=="delete_friend":
            ids = request.POST.getlist('ids',None)
            if not ids:
                return super().post(request, context, *args, **kwargs)

            for i in ids:
                try:
                    f = Friend.objects.get(user=request.user,has_friend=i)
                    f.delete()
                except:
                    pass
                pass

        return super().post(request, context, *args, **kwargs)


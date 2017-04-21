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
from django.db.models import Q
@method_decorator(login_required,name="dispatch")
class PrivateMessageView(AppBaseTemplateView):
    template_name = 'message/private_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_list = UserToUserMessageSession.objects.filter(a_user=self.request.user)
        context['session_list'] = session_list

        u = self.request.GET.get('u',None)

        if not u and not session_list:
            return context
        elif u:
            context['u'] = u
        elif session_list:
            u = session_list[0].b_user.username
            context['u'] = u

        b_user = User.objects.filter(username=u)
        if not b_user:
            return context
        else:
            b_user = b_user[0]
            context['b_user'] = b_user

        # 添加好友
        relationship,c = Friend.objects.get_or_create(user=self.request.user,has_friend=b_user)

        # 添加session
        session,c = UserToUserMessageSession.objects.get_or_create(a_user=self.request.user,b_user=b_user)

        u2u_list = UserToUserMessage.objects.filter(Q(a_user=self.request.user,b_user=b_user)|Q(b_user=self.request.user,a_user=b_user),create_time__gt=session.time)


        change = False
        for i in u2u_list:
            # 标记为已读
            if not i.read and i.b_user==self.request.user:
                change = True
                i.read = True
                i.save()
                self.request.user.messagestatus.minus_user_to_user_message_count()
                session.message_count = session.message_count - 1
                session.save()

        context['u2u_list'] = u2u_list

        if change:
            session_list = UserToUserMessageSession.objects.filter(a_user=self.request.user)
            context['session_list'] = session_list
        return context

    def post(self, request, context={}, *args, **kwargs):

        operation = request.POST.get('operation',None)
        if not operation:
            return super().post(request, context, *args, **kwargs)

        if operation=='send_message':
            message = request.POST.get('message',None)
            if not message:
                return super().post(request, context, *args, **kwargs)
            b_user_id = request.POST.get('b_user_id',None)

            if not b_user_id:
                return super().post(request, context, *args, **kwargs)

            b_user = User.objects.filter(id=b_user_id)
            if not b_user:
                return super().post(request, context, *args, **kwargs)

            b_user = b_user[0]
            a_user = request.user

            #     打开两个会话
            session, c = UserToUserMessageSession.objects.get_or_create(a_user=a_user,b_user=b_user)
            session, c = UserToUserMessageSession.objects.get_or_create(a_user=b_user, b_user=a_user)
            session.message_count = session.message_count + 1
            session.save()


            #     发送消息
            msg = UserToUserMessage()
            msg.content = message
            msg.a_user = a_user
            msg.b_user = b_user
            msg.save()

        #     用户A(主动方)添加B好友
            Friend.objects.get_or_create(user=a_user,has_friend=b_user)

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


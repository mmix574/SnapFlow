from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponseRedirect

from index.appviews import AppBaseTemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required,name="dispatch")
class AdminView(AppBaseTemplateView):
    template_name = 'site_admin/admin.html'

    def get(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse("你不能访问这个网页","")
        return HttpResponseRedirect("/a/add-broadcast/")

    def validate(self):
        user = self.request.user
        if not user.is_authenticated():
            return False
        elif not user.is_staff:
            return False
        else:
            return True

from .models import AdminBroadCast
from index.contrib.response import MessageResponse

@method_decorator(login_required,name="dispatch")
class AdminCreateBroadcastingView(AppBaseTemplateView):
    template_name = 'site_admin/add_broadcast.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        broadcast_list = AdminBroadCast.objects.filter(sended=False)
        context['broadcast_list'] = broadcast_list
        return context

    def get(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse("你不能访问这个网页","")
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse("你不能访问这个网页","")

        tittle = request.POST.get("tittle",None)
        content = request.POST.get("content",None)

        if not tittle or not content:
            return super().post(request, context, *args, **kwargs)
        else:
            abc = AdminBroadCast()
            abc.create_user = request.user
            abc.tittle = tittle
            abc.content = content
            abc.save()

            return super().post(request, context, *args, **kwargs)


    def validate(self):
        user = self.request.user
        if not user.is_authenticated():
            return False
        elif not user.is_staff:
            return False
        else:
            return True

@method_decorator(login_required,name="dispatch")
class AdminSendBroadcastingView(AppBaseTemplateView):
    template_name = 'site_admin/send_broadcast.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        broadcast_list = AdminBroadCast.objects.filter(sended=False)
        context['broadcast_list'] = broadcast_list
        return context

    def post(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse("你不能访问这个网页","")

        operation = request.POST.get('operation',None)
        broadcasts = request.POST.get('_id',None)
        if not operation or not broadcasts:
            return super().post(request, context, *args, **kwargs)

        if operation=="send":
            for i in broadcasts:
                try:
                    bc = AdminBroadCast.objects.get(id=int(i))
                    bc.sended = True
                    bc.save()
                except Exception as e:
                    pass
        elif operation=="delete":
            for i in broadcasts:
                try:
                    bc = AdminBroadCast.objects.get(id=int(i))
                    bc.delete()
                except Exception as e:
                    pass

        return super().post(request, context, *args, **kwargs)

    def get(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse("你不能访问这个网页","")
        return super().get(request, context, *args, **kwargs)

    def validate(self):
        user = self.request.user
        if not user.is_authenticated():
            return False
        elif not user.is_staff:
            return False
        else:
            return True

@method_decorator(login_required,name="dispatch")
class BroadCastHistoryView(AppBaseTemplateView):
    template_name = 'site_admin/broadcast_history.html'

    def get(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse("你不能访问这个网页","")

        broadcast_list = AdminBroadCast.objects.filter(sended=True)
        context['broadcast_list'] = broadcast_list
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse("你不能访问这个网页","")
        return super().post(request, context, *args, **kwargs)

    def validate(self):
        user = self.request.user
        if not user.is_authenticated():
            return False
        elif not user.is_staff:
            return False
        else:
            return True


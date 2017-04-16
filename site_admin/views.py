from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponseRedirect

from index.appviews import AppBaseTemplateView





class AdminView(AppBaseTemplateView):
    template_name = 'site_admin/admin.html'

    def get(self, request, context={}, *args, **kwargs):
        return HttpResponseRedirect("/a/abc")



from .models import AdminBroadCast
from index.contrib.response import MessageResponse


class AdminCreateBroadcastingView(AppBaseTemplateView):
    template_name = 'site_admin/add_broadcast.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        broadcast_list = AdminBroadCast.objects.all()
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

class AdminSendBroadcastingView(AppBaseTemplateView):
    template_name = 'site_admin/send_broadcast.html'
    pass
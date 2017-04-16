from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponseRedirect

from index.appviews import AppBaseTemplateView


class AdminView(AppBaseTemplateView):
    template_name = 'site_admin/admin.html'

    def get(self, request, context={}, *args, **kwargs):
        return HttpResponseRedirect("/a/abc")


class AdminCreateBroadcastingView(AppBaseTemplateView):
    template_name = 'site_admin/add_broadcast.html'
    pass


class AdminSendBroadcastingView(AppBaseTemplateView):
    template_name = 'site_admin/send_broadcast.html'
    pass
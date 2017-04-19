from django.shortcuts import render

# Create your views here.
from index.appviews import AppBaseTemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.http.response import JsonResponse

from .models import History


@method_decorator(login_required,name='dispatch')
class HistoryView(AppBaseTemplateView):
    template_name = 'history/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        history_list = History.objects.filter(user=self.request.user).order_by('-create_time')[:100]
        context['history_list'] = history_list
        context['badge_content'] = "所有问题"
        return context
    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        operation = request.POST.get('operation',None)
        ids = request.POST.getlist('ids',None)
        if not operation or not ids:
            return super().post(request, context, *args, **kwargs)

        print(ids)
        if operation=="delete":
            for i in ids:
                try:
                    h = History.objects.get(id=i,user=request.user)
                    h.delete()
                except Exception as e:
                    pass


        return super().post(request, context, *args, **kwargs)

@method_decorator(login_required,name='dispatch')
class HistoryAskingView(HistoryView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        history_list = History.objects.filter(user=self.request.user,type='asking').order_by('-create_time')[:100]
        context['history_list'] = history_list
        context['badge_content'] = "我的提问"
        return context

@method_decorator(login_required,name='dispatch')
class HistoryAnsweringView(HistoryView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        history_list = History.objects.filter(user=self.request.user,type='answering').order_by('-create_time')[:100]
        context['history_list'] = history_list
        context['badge_content'] = "我的回答"
        return context


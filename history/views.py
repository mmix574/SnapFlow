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
        history_list = History.objects.filter(user=self.request.user).order_by('-create_time')
        context['history_list'] = history_list
        return context
    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        return super().post(request, context, *args, **kwargs)


def add_history(request):
    return JsonResponse({"status":200,"code":200,"message":"添加成功"})

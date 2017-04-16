from django.shortcuts import render

# Create your views here.
from index.appviews import AppBaseTemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.http.response import JsonResponse


@method_decorator(login_required,name='dispatch')
class HistoryView(AppBaseTemplateView):
    template_name = 'history/history.html'
    pass


def add_history(request):
    return JsonResponse({"status":200,"code":200,"message":"添加成功"})

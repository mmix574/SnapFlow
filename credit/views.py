from django.shortcuts import render

# Create your views here.
from index.appviews import AppBaseTemplateView
from django.http.response import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(AppBaseTemplateView):
    template_name = 'credit/index.html'

    def get(self, request, context={}, *args, **kwargs):
        return HttpResponseRedirect("history")
        # return super().get(request, context, *args, **kwargs)

from .models import CreditDefault
@method_decorator(login_required,name="dispatch")
class HistoryView(AppBaseTemplateView):
    template_name = 'credit/history.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        credit_status,c = CreditDefault.objects.get_or_create(user=self.request.user)
        context['credit_status'] = credit_status
        return context

@method_decorator(login_required,name="dispatch")
class ExchangeView(AppBaseTemplateView):
    template_name = 'credit/exchange.html'


@method_decorator(login_required,name="dispatch")
class AchievementView(AppBaseTemplateView):
    template_name = 'credit/achievement.html'

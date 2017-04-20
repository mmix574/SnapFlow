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

from .models import CreditStatus
from .models import CreditLog
@method_decorator(login_required,name="dispatch")
class HistoryView(AppBaseTemplateView):
    template_name = 'credit/history.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        credit_status,c = CreditStatus.objects.get_or_create(user=self.request.user)
        context['credit_status'] = credit_status
        credit_log = CreditLog.objects.filter(user=self.request.user).order_by('-time')[:100]
        context['credit_log'] = credit_log
        return context

    def post(self, request, context={}, *args, **kwargs):
        action = request.POST.get('operation',None)
        if action=="clear_all":
            cl = CreditLog.objects.filter(user=request.user)
            for i in cl:
                i.delete()
        return super().post(request, context, *args, **kwargs)

from .models import CreditStatus
from .models import CreditExchangeCode
from .models import CreditLog
@method_decorator(login_required,name="dispatch")
class ExchangeView(AppBaseTemplateView):
    template_name = 'credit/exchange.html'
    def post(self, request, context={}, *args, **kwargs):
        change_code = request.POST.get('change_code',None)
        if not change_code:
            return super().post(request, context, *args, **kwargs)

        cs , c = CreditStatus.objects.get_or_create(user = request.user)

        context['exchange_status'] = 'success'
        cecs = CreditExchangeCode.objects.filter(code=change_code)

        if not cecs:
            context['exchange_status'] = 'fail'
            return super().post(request, context, *args, **kwargs)
        cec = cecs[0]

        if cec.used:
            context['exchange_status'] = 'fail'
            context['fail_message'] = '你输入的兑换码已经在时间'+str(cec.time)+'兑换了'
            return super().post(request, context, *args, **kwargs)

        cs.credit_point = cs.credit_point + cec.point
        cs.save()
        cl = CreditLog()
        cl.user = request.user
        cl.type = 'exchange'
        cl.brief_content = '您使用了现金兑换码"'+change_code+'"'+'积分增加了'+str(cec.point)
        cl.save()

        cec.used = True
        cec.save()

        context['point_add'] = cec.point

        return super().post(request, context, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cs , c = CreditStatus.objects.get_or_create(user = self.request.user)
        context['current_credit_point'] = cs.credit_point
        return context


@method_decorator(login_required,name="dispatch")
class AchievementView(AppBaseTemplateView):
    template_name = 'credit/achievement.html'

from index.contrib.response import MessageResponse
from credit.models import EverydaySign
from credit.models import CreditLog
@method_decorator(login_required,name="dispatch")
class DoEverydaySign(AppBaseTemplateView):
    template_name = 'credit/signeveryday.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sign = EverydaySign.objects.filter(user=self.request.user)
        signd_today = False
        if not sign or not sign[0].is_today():
            signd_today = False
        else:
            signd_today = True
        context['signd_today'] = signd_today
        return context

    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        operation = request.POST.get('operation',None)
        if not operation:
            return super().post(request, context, *args, **kwargs)
        if operation=='sign':
            sign = EverydaySign.objects.filter(user=self.request.user)
            if not sign or not sign[0].is_today():
                # 打卡
                from .services import do_everyday_sign
                status = do_everyday_sign(request.user)
                print(status,status,status)
                if status:
                    context['success'] = "success"
                else:
                    context['success'] = "fail"
                return super().post(request, context, *args, **kwargs)
            else:
                context['success'] = "fail"
                return super().post(request, context, *args, **kwargs)
        return super().post(request, context, *args, **kwargs)





def check_online_status(user):
    from .models import OnlineLog
    from django.utils import timezone

    minute_span = 1

    # at lease 1
    check_times = 5

    if not user.is_authenticated():
        return
    ols = OnlineLog.objects.today().filter(user=user).order_by('-time')
    count = len(ols)

    if count == 0:
        ol = OnlineLog()
        ol.user = user
        ol.save()
    elif count <=check_times-1:
        last_ol = ols[0]
        minute_passed = (timezone.now() -  last_ol.time).total_seconds()/60
        if minute_passed < minute_span :
            pass
        else:
            ol = OnlineLog()
            ol.user = user
            ol.save()
    elif count ==check_times:
        from credit.models import CreditStatus
        from credit.models import CreditLog

        last_cl = CreditLog.objects.filter(user=user).order_by('-time')

        if not last_cl or not last_cl[0].is_today():

            cs, c = CreditStatus.objects.get_or_create(user=user)
            cs.credit_point = cs.credit_point + 200
            cs.save()
            cl = CreditLog()
            cl.user = user
            cl.type = "online_reward"
            cl.brief_content = "今日在线时长奖励" + ",积分+200"
            cl.save()

    else:
        # donothing
        pass


from django.contrib.auth.models import User
from .models import CreditLog
from .models import EverydaySign
from .models import CreditStatus

def do_everyday_sign(user):
    sign_add_point = 100
    sign = EverydaySign.objects.filter(user=user).order_by('-time')
    if not sign or not sign[0].is_today():
        cs = CreditStatus.objects.get(user=user)
        cs.credit_point = cs.credit_point+sign_add_point
        cs.save()

        cl = CreditLog()
        cl.user = user
        cl.type = 'everyday_sign'
        cl.brief_content = '每日签到,积分'+'+'+str(sign_add_point)
        cl.save()

        es = EverydaySign()
        es.user = user
        es.save()
        return True
    else:
        return False

    return False
def check_online_status(user):
    pass
    # from django.contrib.auth.models import User
    # from .models import OnlineLog
    # from django.utils import timezone
    # if type(user) == int:
    #     try:
    #         user = User.objects.get(id=user)
    #     except Exception as e:
    #         pass
    #
    # try:
    #     if not user.is_authenticated():
    #         return
    # except Exception as e:
    #     pass
    #
    # count = OnlineLog.objects.today().filter(user=user).count()
    #
    # if count >= 4:
    #     return
    # elif count==0:
    #     ol = OnlineLog()
    #     ol.user = user
    #     ol.save()
    # else:
    #     recent_log = OnlineLog.objects.today().filter(user=user).order_by('-time')[0]
    #     recent_time = recent_log.time
    #     now = timezone.now()
    #     minute_delta = (now - recent_time)
    #     dir(minute_delta)
    #     pass




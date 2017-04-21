from django.http.response import JsonResponse



def close_session(request):
    from .models import UserToUserMessageSession
    id = request.GET.get('id',None)
    user = request.user

    if not user.is_authenticated():
        return JsonResponse({'status':400,'message':'用户未登陆','code':2001,'success':False})
    if not id:
        return JsonResponse({'status':400,'message':'缺少id参数','code':4001,'success':False})

    utms = UserToUserMessageSession.objects.filter(id=int(id))
    if not utms:
        return JsonResponse({'status':400,'message':'session id 未找到','code':2002,'success':False})
    utms = utms[0]
    utms.delete()

    return JsonResponse({'status':200,'message':'删除成功','code':2003,'success':True})



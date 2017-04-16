from django.http.response import JsonResponse
from django.http.response import HttpResponse


from .models import ThreadLike
from .models import Thread

def add_like(request):
    user = request.user
    if not user.is_authenticated():
        return JsonResponse({"status":400,"code":400,"message":"用户未登陆","success":False})

    tid = request.GET.get("tid",None)
    if not tid:
        return JsonResponse({"status":201,"code":401,"message":"tid参数不全","success":False})

    thread_instances = Thread.objects.filter(id=tid)
    if not thread_instances:
        return JsonResponse({"status":202,"code":402,"message":'"问题不存在"',"success":False})

    thread_instance = thread_instances[0]
    thread_likes = ThreadLike.objects.filter(thread=thread_instance,user=user)

    if thread_likes:
        thread_like = thread_likes[0]
        thread_like.delete()
        thread_instance.like = thread_instance.like-1
        thread_instance.save()
        return JsonResponse({"status":200,"code":200,"message":"取消赞成功","success":True})
    else:
        _tl = ThreadLike(user=user,thread=thread_instance)
        _tl.save()
        thread_instance.like = thread_instance.like +1
        thread_instance.save()
        return JsonResponse({"status":200,"code":201,"message":"点赞成功","success":True})


from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt



from index.appviews import AppBaseTemplateView
from .models import Collection
from forum.models import Thread


class CollectionView(AppBaseTemplateView):
    template_name = 'collection/collection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection_list = Collection.objects.filter(create_user=self.request.user)
        context['collection_list'] = collection_list
        return context


@csrf_exempt
def add_collection(request):
    user = request.user
    logined = user.is_authenticated()

    if not logined:
        return JsonResponse({"code":400,"message":"你还没有登录","success":False})

    tid = request.GET.get('tid',None)
    if not tid:
        return JsonResponse({"code":401,"message":"缺少参数tid","success":False})


    thread_find = Thread.objects.filter(id=tid)

    if not thread_find:
        return JsonResponse({"code": 402, "message": "tid不正确", "success": False})


    logs = Collection.objects.filter(thread=thread_find[0],create_user=request.user)
    if logs:
        return JsonResponse({"code":201,"message":"请勿重复添加","success":False})

    c = Collection()
    c.create_user = request.user
    c.thread = thread_find[0]
    c.save()
    return JsonResponse({"code":200,"message":"成功","success":True})

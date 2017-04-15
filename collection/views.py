from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt



from index.appviews import AppBaseTemplateView


class CollectionView(AppBaseTemplateView):
    template_name = 'collection/collection.html'


@csrf_exempt
def add_collection(request):
    user = request.user
    logined = user.is_authenticated()

    if not logined:
        return JsonResponse({"code":400,"message":"你还没有登录","success":False})




    return JsonResponse({"code":200,"message":"成功","success":True})

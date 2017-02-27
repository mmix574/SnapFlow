from django.http.response import JsonResponse
from django.http.response import HttpResponse

from django.views.generic.base import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(csrf_exempt, name='dispatch')
class ApiView(View):
    # 默认错误
    OperateErrorDict = {"status": 500, "message": "default server error: operation error Or unimplement method calling"}

    # JSON 解析错误
    JsonValidateDict = {"status":400,"message":"Posting Json is Not completely a JSON,please check json agagin"}

    OperateError = JsonResponse(OperateErrorDict)
    JsonValidateError = JsonResponse(JsonValidateDict)

    # 默认返回 '默认错误'
    def get(self, request):
        return JsonResponse(self.OperateErrorDict)
    def post(self,request):
        return JsonResponse(self.OperateErrorDict)

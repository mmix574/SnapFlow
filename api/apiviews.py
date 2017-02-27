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
    # default response
    def get(self, request):
        return JsonResponse(self.OperateErrorDict)
    def post(self,request):
        return JsonResponse(self.OperateErrorDict)


    # error handel
    def AcceptResponseWithMessage(self,message):
        resp = {"status":200,"message":message}
        return JsonResponse(resp)

    def ServerSideErrorWithMessage(self,message):
        resp = {"status":500,"message":message}
        return JsonResponse(resp)

    def ClientSideErrorWithMessage(self,message):
        resp = {"status":400,"message":message}
        return JsonResponse(resp)

    # 其他信息存储在data 下
    def BaseAcceptResponse(self,message,data):
        resp = {"status":200,"message":message,"data":data}
        return JsonResponse(resp)


    # !!!!!!!!!!!!!!!!!!!!!!!
    # 全部使用这个json response
    # 2017年2月27日 15:25:26
    def V2Response(self,status=200,success=False,message="None",code=-1,otherStatement="None",otherData={}):

        data = {"otherStatement":otherStatement}
        data.update(otherData)
        resp = {"status":status,"code":code,"success":success,"message":message,"data":data}
        return JsonResponse(resp)
    def V2ResponseShortCut(self,success,code,message):
        return self.V2Response(success=success,code=code,message=message)

    # def V3Response(self):
    #     resp = {"status":406,"message":"not implement yet"}
    #     return JsonResponse(resp)
from django.shortcuts import render
from django.core.serializers import serialize,deserialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from . import apiviews

from django.http.response import JsonResponse


import json


OperateErrorJson = {"status":400,"message":"operation error"}

def messageHandel(status,message):
    msg = {"status":status,"message":message}
    return HttpResponse(json.dumps(msg))


# ---------------------------------------------
from website.utils import console
@csrf_exempt
def user_validate(request):
    if(request.method=="GET"):
        jsonStr = {'isSuccess':False}
        return HttpResponse(json.dumps(jsonStr))
    elif(request.method=="POST"):

        try:
            body_unicode = request.body.decode('utf-8')
            obj = json.loads(body_unicode)

            # obj = json.loads(requestJson)
        except Exception as e:
            # raise e
            return messageHandel(400,"Json Parse Error")
            pass
        if("password" in obj and "username" in obj):
            user = authenticate(username = obj["username"],password = obj["password"])

            console.log(obj["username"])
            console.log(obj["password"])

            if(user):
                res = {"status":200,"message":"success","data":{"is_success":True,"username":obj["username"]}}
                return HttpResponse(json.dumps(res));
            else:
                res = {"status":200,"message":"fail","data":{"is_success":False}}
                return HttpResponse(json.dumps(res))
        else:
            return messageHandel(400,"username or password not found")
    else:
        return HttpResponse(json.dumps(OperateErrorJson))

@csrf_exempt
def default(request):
    jsonStr = {"status":400,"message":"no specify any operation"}
    return HttpResponse(json.dumps(jsonStr))


# class UserRegisterView()



class UserRegisterView(apiviews.ApiView):

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            user_data = json.loads(body_unicode)

        except Exception:
            return self.JsonValidateError

        email = user_data.get('email',None)
        username = user_data.get('username',None)
        password = user_data.get('password',None)

        if(email and username and password):
            user_exist = True
            try:
                User.objects.get(username=username)
            except ObjectDoesNotExist:
                user_exist = False

            if user_exist:
                return self.V2Response(code=1001,success=False,message="用户名已存在，请重新输入")
        else:
            return self.V2Response(status=400,code=1002, success=False, message="用户信息不完整，请重试")

        # 在里开始
        user = User.objects.create(username=username,email=email)
        user.set_password(password)
        user.save()

        return self.V2ResponseShortCut(True,2001,"用户注册成功!")


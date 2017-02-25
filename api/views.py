from django.shortcuts import render
from django.core.serializers import serialize,deserialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json

OperateErrorJson = {"status":400,"message":"operation error"}

def messageHandel(status,message):
    msg = {"status":status,"message":message}
    return HttpResponse(json.dumps(msg))


# ---------------------------------------------

@csrf_exempt
def user_validate(request):
    if(request.method=="GET"):
        jsonStr = {'isSuccess':False}
        return HttpResponse(json.dumps(jsonStr))
    elif(request.method=="POST"):
        requestJson = request.body

        try:
            obj = json.loads(requestJson)
        except Exception as e:
            # raise e
            return messageHandel(400,"Json Parse Error")
            pass
        if("password" in obj and "username" in obj):
            user = authenticate(username = obj["username"],password = obj["password"])
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


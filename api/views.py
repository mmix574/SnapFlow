from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth.models import User
import json


@csrf_exempt
def user(request):
    dic = {'a':1,'b':2}
    if(request.method=='POST'):
        print(request.body)

        return HttpResponse(serialize('json',dic))
    else:
        print(request.method)
    return HttpResponse(json.dumps(dic))


def default(request):
    return HttpResponse("default api calling ")

